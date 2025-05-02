import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for user registration."""
    username: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str


class UserRead(BaseModel):
    """Schema for reading user info."""
    id: uuid.UUID
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    """Schema for updating user info."""
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
