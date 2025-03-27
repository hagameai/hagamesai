from pydantic import BaseModel, EmailStr
from typing import Optional

class UserProfile(BaseModel):
    id: int
    user_id: int  # Foreign key to associate with User
    display_name: str
    bio: Optional[str] = None
    email: Optional[EmailStr] = None  # Email validation
    profile_picture: Optional[str] = None  # URL to profile picture

    class Config:
        orm_mode = True  # Allows compatibility with ORM

class UserProfileCreate(BaseModel):
    user_id: int
    display_name: str
    bio: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[str] = None

class UserProfileUpdate(BaseModel):
    display_name: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[str] = None
