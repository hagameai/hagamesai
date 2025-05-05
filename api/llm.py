from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from llm_service.schemas import LLMCallRequest, LLMCallResponse, LLMCallLogRead
from llm_service.service import LLMIntegrationService
from llm_service.crud import create_log, list_logs_by_user
from core.database import get_async_session
from core.auth import get_current_user
from core.logging import get_logger
from core.tasks import call_llm_task
from schemas.task import TaskStatus
import uuid

logger = get_logger(__name__)
# llm_service = LLMIntegrationService() # No longer instantiated directly in endpoint

router = APIRouter(prefix="/llm", tags=["llm"])


@router.post("/call", response_model=TaskStatus, summary="Trigger async LLM API call")
async def call_llm_endpoint(
    req: LLMCallRequest,
    current_user=Depends(get_current_user),
) -> TaskStatus:
    """Trigger an asynchronous LLM API call and return the task ID."""
    logger.info(
        f"User {current_user.email} triggering async LLM call: {req.provider}/{req.model}")
    # Attach user_id to request data for the task
    req_data = req.dict()
    # Pass UUID as string for serialization
    req_data["user_id"] = str(current_user.id)

    # Trigger the Celery task
    task = call_llm_task.delay(req_data)

    # Return the task status immediately
    return TaskStatus(task_id=task.id, status=task.status)


@router.get("/logs", response_model=list[LLMCallLogRead], summary="List user's LLM call logs")
async def get_logs(
    session: AsyncSession = Depends(get_async_session),
    current_user=Depends(get_current_user),
):
    """List all LLM call logs for the current user."""
    logger.info(f"Listing LLM call logs for user: {current_user.email}")
    logs = await list_logs_by_user(session, current_user.id)
    # Ensure orm_mode is True on LLMCallLogRead for serialization
    return [LLMCallLogRead.from_orm(log) for log in logs]
