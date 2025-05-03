from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from llm_service.schemas import LLMCallRequest, LLMCallResponse, LLMCallLogRead
from llm_service.service import LLMIntegrationService
from llm_service.crud import create_log, list_logs_by_user
from core.database import get_async_session
from core.auth import get_current_user
from core.logging import get_logger
import uuid

logger = get_logger(__name__)
llm_service = LLMIntegrationService()

router = APIRouter(prefix="/llm", tags=["llm"])


@router.post("/call", response_model=LLMCallResponse, summary="Call LLM API")
async def call_llm(
    req: LLMCallRequest,
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """Call an LLM API and log the request/response."""
    logger.info(
        f"User {current_user.email} calling LLM: {req.provider}/{req.model}")
    # Attach user_id to request
    req.user_id = current_user.id
    result = await llm_service.call_llm(req)
    await create_log(session, req, result.response, result.status)
    return result


@router.get("/logs", response_model=list[LLMCallLogRead], summary="List user's LLM call logs")
async def get_logs(
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """List all LLM call logs for the current user."""
    logger.info(f"Listing LLM call logs for user: {current_user.email}")
    logs = await list_logs_by_user(session, current_user.id)
    return [LLMCallLogRead.from_orm(log) for log in logs]
