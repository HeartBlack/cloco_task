from datetime import datetime
from typing import Optional
from fastapi import File, Form, UploadFile, status
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from auth.get_current_user import check_user_type
from models.models import Album, Role, Songs
from extension import get_db
from fastapi_pagination import Params, paginate

router = APIRouter()


@router.get("/get_all_songs/")
def get_all_songs(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
):
    query = db.query(Songs).all()
    params = Params(page=page, page_size=page_size)
    songs = paginate(query, params=params)

    for song in songs.items:
        if song.audio_file:
            song.audio_file = f"/audio/{song.title}/{song.audio_file}"

    return songs


@router.post("/create_songs/")
def create_songs(
    title: str = Form(...),
    song_name: str | None = Form(None),
    song_description: str | None = Form(None),
    song_url: str | None = Form(None),
    album: int = Form(),
    audio_file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(check_user_type([Role.ARTIST, Role.ADMIN])),
):
    album = db.query(Album).filter_by(id=album).first()

    if album and album.artist == current_user.id:
        songs = Songs(
            title=title,
            song_name=song_name,
            song_description=song_description,
            song_url=song_url,
        )
        file_path = songs.saving_artist_mp3(audio_file, album.title)
        songs.audio_file = file_path

        db.add(songs)
        db.commit()
        db.refresh(instance=songs)
        return songs
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")


@router.get("/get_songs_by_id/{id}")
def get_songs_by_id(id, db: Session = Depends(get_db)):
    query = db.query(Songs).filter_by(id=id).first()
    if query:
        return query
    return {"data": "Album is not found"}


@router.put("/update_song/{id}")
def update_song(
    id: int,
    title: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    first_release_year: Optional[datetime] = Form(None),
    no_of_released: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    current_user=Depends(check_user_type([Role.ARTIST, Role.ADMIN])),
):
    query = db.query(Songs).filter_by(id=id).first()

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


@router.delete("/delete_song/{id}")
def delete_song(
    id: int,
    db: Session = Depends(get_db),
    dependencies=Depends(check_user_type([Role.ARTIST, Role.ADMIN])),
):
    query = db.query(Songs).filter_by(id=id).first()
    if query:
        db.delete(query)
        db.commit()
        return {"data": "Song is deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")


@router.get("/audio/")
async def serve_audio_file(title: str = Query(...), db: Session = Depends(get_db)):
    song = db.query(Songs).filter(Songs.title.ilike(f"%{title}%")).first()
    if song:
        # pass
        file_path = f"audio/{song.audio_file}"
        print(file_path)
    else:
        return {"message": "Song not found"}
