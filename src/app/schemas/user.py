from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    username: str = None
    email: Optional[EmailStr] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    name: str
    email: EmailStr
    password: str
    confirmed_password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    confirmed_password: Optional[str] = None


class UserLogin(UserBase):
    username: str
    password: str


class UserInDBBase(UserBase):
    id: Optional[int] = None
    name: str

    class Config:
        from_attributes = True


# Additional properties to return via API
class User(UserInDBBase):
    name: str

# Additional properties stored in DB


class UserInDB(UserInDBBase):
    password: str
