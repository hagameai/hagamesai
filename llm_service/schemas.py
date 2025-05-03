import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class LLMCallRequest(BaseModel):
    """Schema for making an LLM call."""
    provider: str = Field(..., max_length=50)
    model: str = Field(..., max_length=100)
    prompt: str
    user_id: uuid.UUID | None = None


class LLMCallResponse(BaseModel):
    """Schema for LLM call response."""
    response: str
    status: str


class LLMCallLogRead(BaseModel):
    """Schema for reading LLM call log info."""
    id: uuid.UUID
    user_id: uuid.UUID | None
    provider: str
    model: str
    prompt: str
    response: str | None
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
