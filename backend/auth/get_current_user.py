from typing import List
from fastapi import Depends, HTTPException,status
from jose import JWTError,jwt
from auth.authenticate_user import get_user
from extension import get_db
from sqlalchemy.orm import Session
from models.models import User,Role
from config import Config

def get_current_user(token: str = Depends(Config.oauth2_scheme),db: Session=Depends(get_db)):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    user = get_user(username,db)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user


def check_user_type(user_types: List[Role] = None):
    def user_type_dependency(current_user = Depends(get_current_user)):
        if user_types and current_user.user_type not in user_types:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not Unauthorized")
        
        return current_user
    
    return user_type_dependency