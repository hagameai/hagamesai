import uuid
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from models.user import Base


class AIModel(Base):
    """AIModel model for storing AI model configuration and metadata."""
    __tablename__ = "ai_models"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    version: Mapped[str] = mapped_column(String(20), nullable=False)
    config_params: Mapped[dict] = mapped_column(
        JSONB, nullable=False, default=dict)
    file_path: Mapped[str | None] = mapped_column(String(255), nullable=True)
