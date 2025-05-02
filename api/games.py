from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.game_definition import GameDefinitionCreate, GameDefinitionRead
from schemas.game_instance import GameInstanceCreate, GameInstanceRead
from crud.game_definition import get_by_id as get_game_def_by_id, create as create_game_def, list_all as list_game_defs
from crud.game_instance import get_by_id as get_instance_by_id, create as create_instance, list_by_user as list_instances_by_user
from core.database import get_async_session
from core.auth import get_current_user
from core.logging import get_logger
import uuid

logger = get_logger(__name__)

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/definitions", response_model=list[GameDefinitionRead], summary="List all game definitions")
async def list_definitions(session: AsyncSession = Depends(get_async_session)):
    """List all available game definitions."""
    logger.info("Listing all game definitions")
    return [GameDefinitionRead.from_orm(g) for g in await list_game_defs(session)]


@router.post("/definitions", response_model=GameDefinitionRead, status_code=status.HTTP_201_CREATED, summary="Create a new game definition")
async def create_definition(
    data: GameDefinitionCreate,
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """Create a new game definition (admin only in future)."""
    logger.info(
        f"User {current_user.email} creating game definition: {data.name}")
    game_def = await create_game_def(session, data)
    return GameDefinitionRead.from_orm(game_def)


@router.get("/definitions/{game_def_id}", response_model=GameDefinitionRead, summary="Get game definition by ID")
async def get_definition(game_def_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    """Get a game definition by its ID."""
    game_def = await get_game_def_by_id(session, game_def_id)
    if not game_def:
        logger.warning(f"Game definition not found: {game_def_id}")
        raise HTTPException(
            status_code=404, detail="Game definition not found.")
    return GameDefinitionRead.from_orm(game_def)


@router.post("/instances", response_model=GameInstanceRead, status_code=status.HTTP_201_CREATED, summary="Create a new game instance")
async def create_game_instance(
    data: GameInstanceCreate,
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """Create a new game instance for the current user."""
    logger.info(
        f"User {current_user.email} creating game instance for game_def {data.game_definition_id}")
    instance = await create_instance(session, data)
    return GameInstanceRead.from_orm(instance)


@router.get("/instances/{instance_id}", response_model=GameInstanceRead, summary="Get game instance by ID")
async def get_game_instance(instance_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    """Get a game instance by its ID."""
    instance = await get_instance_by_id(session, instance_id)
    if not instance:
        logger.warning(f"Game instance not found: {instance_id}")
        raise HTTPException(status_code=404, detail="Game instance not found.")
    return GameInstanceRead.from_orm(instance)


@router.get("/my-instances", response_model=list[GameInstanceRead], summary="List current user's game instances")
async def list_my_instances(
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """List all game instances for the current user."""
    logger.info(f"Listing game instances for user: {current_user.email}")
    return [GameInstanceRead.from_orm(i) for i in await list_instances_by_user(session, current_user.id)]
