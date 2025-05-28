import uuid
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class AIModelBase(BaseModel):
    name: str
    description: Optional[str] = None
    config: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None
    file_path: Optional[str] = None


class AIModelCreate(AIModelBase):
    """Schema for creating a new AI model."""
    type: str = Field(..., max_length=50)
    version: str = Field(..., max_length=20)


class AIModelUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    file_path: Optional[str] = None


class AIModelRead(AIModelBase):
    """Schema for reading AI model info."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
