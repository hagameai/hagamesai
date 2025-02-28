from pydantic import BaseModel, Field
from typing import Optional

class GameInstance(BaseModel):
    id: int = Field(..., description="Unique identifier for the game instance")
    game_id: int = Field(..., description="Identifier for the associated game")
    user_id: int = Field(..., description="Identifier for the user playing this game instance")
    status: str = Field(..., description="Current status of the game instance (e.g., 'in_progress', 'completed')")
    created_at: str = Field(..., description="Timestamp when the game instance was created")
    updated_at: Optional[str] = Field(None, description="Timestamp when the game instance was last updated")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "game_id": 101,
                "user_id": 201,
                "status": "in_progress",
                "created_at": "2023-01-01T12:00:00Z",
                "updated_at": "2023-01-01T12:30:00Z"
            }
        }
