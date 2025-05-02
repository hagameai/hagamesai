import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class CognitiveProfileRead(BaseModel):
    """Schema for reading cognitive profile info."""
    id: uuid.UUID
    user_id: uuid.UUID
    profile_data: dict
    last_updated: datetime


class CognitiveProfileUpdate(BaseModel):
    """Schema for updating cognitive profile info."""
    profile_data: dict = Field(...)
