from datetime import datetime
from typing import Optional
from fastapi import Form, status
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session
from auth.get_current_user import check_user_type, get_current_user
from models.models import Album, Role, User
from extension import get_db
from fastapi_pagination import Params, paginate

router = APIRouter()


@router.get("/get_album/")
def get_all_album(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
):
    query = db.query(Album).all()
    params = Params(page=page, page_size=page_size)
    albums = paginate(query, params=params)
    return albums


@router.post("/create_album/")
def create_album(
    title: str = Form(...),
    description: str | None = Form(None),
    first_release_year: str | None = Form(None),
    no_of_released: str | None = Form(None),
    db: Session = Depends(get_db),
    current_user=Depends(check_user_type([Role.ARTIST, Role.ADMIN])),
):
    album = Album(
        title=title,
        description=description,
        first_release_year=first_release_year,
        artist=current_user.id,
        no_of_released=no_of_released,
    )
    db.add(album)
    db.commit()
    return {
        "message": "album is created",
        "data": {
            "title": title,
            "description": description,
            "first_release_year": first_release_year,
            "no_of_released": no_of_released,
            "created_by": current_user.username,
        },
    }


@router.get("/get_album/{id}")
def get_album_by_id(id, db: Session = Depends(get_db)):
    query = db.query(Album).filter_by(id=id).first()
    if query:
        return query
    return {"data": "Album is not found"}


@router.put("/update_album/")
def update_album(
    id: int = Form(...),
    title: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    first_release_year: Optional[datetime] = Form(None),
    no_of_released: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    current_user=Depends(check_user_type([Role.ARTIST, Role.ADMIN])),
):
    query = db.query(Album).filter_by(id=id).first()

    if query:
        if title is not None:
            query.title = title
        if description is not None:
            query.description = description
        if first_release_year is not None:
            query.first_release_year = first_release_year
        if no_of_released is not None:
            query.no_of_released = no_of_released

        db.commit()
        db.refresh(instance=query)
        return query

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")


@router.delete("/delete_album/{id}")
def delete_album_by_id(
    id: int,
    db: Session = Depends(get_db),
    dependencies=Depends(check_user_type([Role.ARTIST, Role.ADMIN])),
):
    query = db.query(Album).filter_by(id=id).first()
    if query:
        db.delete(query)
        db.commit()
        return {"data": "Album is deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
