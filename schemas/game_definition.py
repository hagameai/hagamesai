import uuid
from pydantic import BaseModel, Field


class GameDefinitionCreate(BaseModel):
    """Schema for creating a new game definition."""
    name: str = Field(..., max_length=100)
    description: str
    rules_config: dict
    version: str = Field(..., max_length=20)


class GameDefinitionRead(BaseModel):
    """Schema for reading game definition info."""
    id: uuid.UUID
    name: str
    description: str
    rules_config: dict
    version: str

    class Config:
        orm_mode = True
