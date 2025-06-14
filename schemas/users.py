from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name : str
    email : EmailStr
    
class UserCreate(UserBase):
    pass

class Users(UserBase):
    id : int
    is_active : bool = True

class UserUpdate(BaseModel):
    name : Optional[str] = None
    email : Optional[EmailStr] = None
    is_active : Optional[bool] = True
