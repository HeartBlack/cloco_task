import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "aaklghkashghalghlashgahslghlahgl")
    POSTGRES_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/cloco_db"
    )
    engine = create_engine(POSTGRES_DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/")
