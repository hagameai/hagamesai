from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ai_model import AIModelCreate, AIModelRead
from crud.ai_model import get_by_id, create, list_all
from core.database import get_async_session
from core.auth import get_current_user
from core.logging import get_logger
import uuid

logger = get_logger(__name__)

router = APIRouter(prefix="/ai-models", tags=["ai"])


@router.get("/", response_model=list[AIModelRead], summary="List all AI models")
async def list_models(session: AsyncSession = Depends(get_async_session)):
    """List all available AI models."""
    logger.info("Listing all AI models")
    return [AIModelRead.from_orm(m) for m in await list_all(session)]


@router.post("/", response_model=AIModelRead, status_code=status.HTTP_201_CREATED, summary="Create a new AI model")
async def create_model(
    data: AIModelCreate,
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """Create a new AI model (admin only in future)."""
    logger.info(f"User {current_user.email} creating AI model: {data.name}")
    model = await create(session, data)
    return AIModelRead.from_orm(model)


@router.get("/{model_id}", response_model=AIModelRead, summary="Get AI model by ID")
async def get_model(model_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    """Get an AI model by its ID."""
    model = await get_by_id(session, model_id)
    if not model:
        logger.warning(f"AI model not found: {model_id}")
        raise HTTPException(status_code=404, detail="AI model not found.")
    return AIModelRead.from_orm(model)
