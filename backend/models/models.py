import os
import sqlalchemy as db
from config import Config
from sqlalchemy.orm import relationship
from enum import Enum
from datetime import datetime
from fastapi import HTTPException, UploadFile

Base = Config.Base


class Role(Enum):
    ADMIN = "admin"
    ARTIST = "artist"
    NORMAL = "normal"


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    first_name = db.Column(
        db.String,
        nullable=True,
    )
    last_name = db.Column(db.String, nullable=True)
    dob = db.Column(db.DateTime, nullable=True)
    user_type = db.Column(db.Enum(Role), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True
    )


class Album(Base):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text, nullable=True)
    artist = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    first_release_year = db.Column(db.DateTime, nullable=True)
    no_of_released = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True
    )

    art = relationship("User", backref="albums")


class Songs(Base):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True, index=True)
    album = db.Column(db.ForeignKey("albums.id"), nullable=True)
    title = db.Column(db.Text, nullable=True)
    song_name = db.Column(db.Text, nullable=True)
    song_description = db.Column(db.Text, nullable=True)
    song_url = db.Column(db.Text, nullable=True)
    audio_file = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True
    )
    _albums = relationship("Album", backref="songs")

    def saving_artist_mp3(self, audio_file: UploadFile, album_name):
        if audio_file.filename.endswith(".mp3"):
            file_directory = f"static/{album_name}"
            os.makedirs(file_directory, exist_ok=True)
            file_path = os.path.join(file_directory, audio_file.filename)
            with open(file_path, "wb") as file:
                file.write(audio_file.file.read())

            return file_path
        else:
            raise HTTPException(
                status_code=400, detail="Invalid file format. Only MP3 files are allowed."
            )
