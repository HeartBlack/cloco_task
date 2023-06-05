from datetime import datetime, timedelta
from typing import Optional
from fastapi import Form, status
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import ValidationError
from sqlalchemy import or_
from sqlalchemy.orm import Session
from auth.authenticate_user import authenticate_user, create_access_token
from auth.get_current_user import check_user_type, get_current_user
from models.models import Album, Role, User
from extension import get_db, get_password_hash
from schema.schema import create_user
from fastapi_pagination import Page, Params, paginate
from config import Config

router = APIRouter()


@router.post("/register/")
def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    password2: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        user_form = create_user(
            username=username, email=email, password=password, password2=password2
        )
    except ValidationError as e:
        return e.errors()

    user_exists = (
        db.query(User)
        .filter(or_(User.username == user_form.username, User.email == user_form.email))
        .first()
    )
    if user_exists:
        return {"message", "username or email is already registerd"}
    data = user_form.dict()
    password = data.pop("password")
    hashed_password = get_password_hash(password)
    user = User(
        username=user_form.username,
        email=user_form.email,
        password=hashed_password,
        user_type=None,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully."}


@router.post("/login/")
def login(
    username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)
):
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


