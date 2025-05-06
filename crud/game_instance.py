import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.game_instance import GameInstance
from schemas.game_instance import GameInstanceCreate


async def get_by_id(session: AsyncSession, id: uuid.UUID) -> GameInstance | None:
    """Get a game instance by id."""
    result = await session.execute(select(GameInstance).where(GameInstance.id == id))
    return result.scalars().first()


async def create(session: AsyncSession, data: GameInstanceCreate) -> GameInstance:
    """Create a new game instance."""
    instance = GameInstance(
        game_definition_id=data.game_definition_id,
        user_id=data.user_id,
        game_state=data.game_state,
        ai_model_id=data.ai_model_id
    )
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


async def list_by_user(session: AsyncSession, user_id: uuid.UUID) -> list[GameInstance]:
    """List all game instances for a user."""
    result = await session.execute(select(GameInstance).where(GameInstance.user_id == user_id))
    return result.scalars().all()
