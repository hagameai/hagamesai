import uuid
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from models.user import Base


class GameDefinition(Base):
    """GameDefinition model for storing game metadata and rules."""
    __tablename__ = "game_definitions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rules_config: Mapped[dict] = mapped_column(
        JSONB, nullable=False, default=dict)
    version: Mapped[str] = mapped_column(String(20), nullable=False)
