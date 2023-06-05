from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from fastapi import Depends
from extension import get_db, verify_password
from models.models import User
from schema.schema import create_user
from jose import JWTError, jwt
from config import Config


def get_user(username: str, db: Session):
    user = db.query(User).filter_by(username=username).first()
    if user:
        return user
    else:
        return None


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
    return encoded_jwt
