import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.game_definition import GameDefinition
from schemas.game_definition import GameDefinitionCreate


async def get_by_id(session: AsyncSession, id: uuid.UUID) -> GameDefinition | None:
    """Get a game definition by id."""
    result = await session.execute(select(GameDefinition).where(GameDefinition.id == id))
    return result.scalars().first()


async def get_by_name(session: AsyncSession, name: str) -> GameDefinition | None:
    """Get a game definition by name."""
    result = await session.execute(select(GameDefinition).where(GameDefinition.name == name))
    return result.scalars().first()


async def create(session: AsyncSession, data: GameDefinitionCreate) -> GameDefinition:
    """Create a new game definition."""
    game_def = GameDefinition(
        name=data.name,
        description=data.description,
        rules_config=data.rules_config,
        version=data.version
    )
    session.add(game_def)
    await session.commit()
    await session.refresh(game_def)
    return game_def


async def list_all(session: AsyncSession) -> list[GameDefinition]:
    """List all game definitions."""
    result = await session.execute(select(GameDefinition))
    return result.scalars().all()
