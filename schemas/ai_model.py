import uuid
from pydantic import BaseModel, Field


class AIModelCreate(BaseModel):
    """Schema for creating a new AI model."""
    name: str = Field(..., max_length=100)
    type: str = Field(..., max_length=50)
    version: str = Field(..., max_length=20)
    config_params: dict
    file_path: str | None = None


class AIModelRead(BaseModel):
    """Schema for reading AI model info."""
    id: uuid.UUID
    name: str
    type: str
    version: str
    config_params: dict
    file_path: str | None

    class Config:
        orm_mode = True
