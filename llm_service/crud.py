import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from llm_service.models import LLMCallLog
from llm_service.schemas import LLMCallRequest


async def create_log(session: AsyncSession, req: LLMCallRequest, response: str, status: str) -> LLMCallLog:
    """Create a new LLM call log entry."""
    log = LLMCallLog(
        user_id=req.user_id,
        provider=req.provider,
        model=req.model,
        prompt=req.prompt,
        response=response,
        status=status
    )
    session.add(log)
    await session.commit()
    await session.refresh(log)
    return log


async def list_logs_by_user(session: AsyncSession, user_id: uuid.UUID) -> list[LLMCallLog]:
    """List all LLM call logs for a user."""
    result = await session.execute(select(LLMCallLog).where(LLMCallLog.user_id == user_id))
    return result.scalars().all()
