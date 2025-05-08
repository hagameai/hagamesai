import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class GameInstanceCreate(BaseModel):
    """Schema for creating a new game instance."""
    game_definition_id: uuid.UUID
    user_id: uuid.UUID | None = None
    game_state: dict = Field(default_factory=dict)
    ai_model_id: uuid.UUID | None = None


class GameInstanceRead(BaseModel):
    """Schema for reading game instance info."""
    id: uuid.UUID
    game_definition_id: uuid.UUID
    user_id: uuid.UUID | None
    status: str
    game_state: dict
    start_time: datetime
    end_time: datetime | None
    score: int | None
    ai_model_id: uuid.UUID | None

    class Config:
        orm_mode = True
