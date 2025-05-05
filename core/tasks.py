# Define Celery tasks here

from core.celery_app import celery_app
import time
import logging
from llm_service.schemas import LLMCallRequest, LLMCallResponse
# Import the service to use its logic
from llm_service.service import LLMIntegrationService
from sqlalchemy.ext.asyncio import AsyncSession
# Need async session in task if logging to DB
from core.database import get_async_session
from llm_service.crud import create_log

logger = logging.getLogger(__name__)


@celery_app.task
def example_task(seconds: int):
    """An example Celery task that sleeps for a specified number of seconds."""
    logger.info(f"Starting example task, sleeping for {seconds} seconds...")
    time.sleep(seconds)
    logger.info("Example task finished.")
    return f"Slept for {seconds} seconds"


@celery_app.task(bind=True)
async def call_llm_task(self, req_data: dict):
    """Celery task to make an LLM API call and log the result."""
    # Recreate Pydantic object from dict data
    req = LLMCallRequest(**req_data)
    logger.info(
        f"Starting LLM call task for {req.provider}/{req.model} by user {req.user_id}")

    # Instantiate the service and call the mock LLM logic
    # Note: In a real scenario, handling DB sessions and other dependencies
    # inside a Celery task requires careful consideration, often using
    # the task's `request` or a separate session management approach.
    # For simplicity here, we'll use a new session for logging.
    llm_service = LLMIntegrationService()
    result = await llm_service.call_llm(req)

    # Log the result to the database within the task
    try:
        # Need to create a new async session for the task context
        async for session in get_async_session():
            await create_log(session, req, result.response, result.status)
            # Session commit is handled by create_log
        logger.info(
            f"LLM call task finished with status {result.status} for {req.provider}/{req.model}")
    except Exception as e:
        logger.error(f"Error logging LLM call result in task: {e}")
        # Consider retrying the task if logging fails critically
        # self.retry(exc=e, countdown=60)

    return result.dict()  # Return result as dict for serialization
