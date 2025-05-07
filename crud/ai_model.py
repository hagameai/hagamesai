import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ai_model import AIModel
from schemas.ai_model import AIModelCreate


async def get_by_id(session: AsyncSession, id: uuid.UUID) -> AIModel | None:
    """Get an AI model by id."""
    result = await session.execute(select(AIModel).where(AIModel.id == id))
    return result.scalars().first()


async def create(session: AsyncSession, data: AIModelCreate) -> AIModel:
    """Create a new AI model."""
    model = AIModel(
        name=data.name,
        type=data.type,
        version=data.version,
        config_params=data.config_params,
        file_path=data.file_path
    )
    session.add(model)
    await session.commit()
    await session.refresh(model)
    return model


async def list_all(session: AsyncSession) -> list[AIModel]:
    """List all AI models."""
    result = await session.execute(select(AIModel))
    return result.scalars().all()
