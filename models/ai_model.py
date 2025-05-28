import uuid
from sqlalchemy import String, Text, Column, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from models.user import Base


class AIModel(Base):
    """AIModel model for storing AI model configuration and metadata."""
    __tablename__ = "ai_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    config = Column(JSON, nullable=False)
    metadata = Column(JSON, nullable=True)
    file_path = Column(String, nullable=True)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=True)
