from datetime import datetime
from typing import Optional,List
from pydantic import BaseModel,EmailStr, validator,Field,ValidationError,datetime_parse



class create_user(BaseModel):
    username : str
    email : EmailStr
    password: str = Field(..., min_length=2)
    password2: str = Field(..., min_length=2)

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError({"message":'passwords do not match'})
        return v




    class Config:
        orm_mode = True


class login_access(BaseModel):
    username: str
    password: str

