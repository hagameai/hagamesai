from pydantic import BaseModel, Field
from typing import List, Optional

class GameDefinition(BaseModel):
    id: int = Field(..., description="Unique identifier for the game definition")
    name: str = Field(..., description="Name of the game")
    description: Optional[str] = Field(None, description="Description of the game")
    rules: str = Field(..., description="Rules of the game")
    created_at: str = Field(..., description="Timestamp of when the game was created")
    updated_at: str = Field(..., description="Timestamp of when the game was last updated")

class GameDefinitionCreate(BaseModel):
    name: str = Field(..., description="Name of the game")
    description: Optional[str] = Field(None, description="Description of the game")
    rules: str = Field(..., description="Rules of the game")

class GameDefinitionUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Name of the game")
    description: Optional[str] = Field(None, description="Description of the game")
    rules: Optional[str] = Field(None, description="Rules of the game")

class GameDefinitionResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    rules: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
