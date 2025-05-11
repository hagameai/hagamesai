from fastapi import APIRouter, Depends, HTTPException, status
from schemas.task import TaskTrigger, TaskStatus
from core.tasks import example_task
from core.logging import get_logger
from celery.result import AsyncResult

logger = get_logger(__name__)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/example", response_model=TaskStatus, summary="Trigger example async task")
async def trigger_example_task(task_in: TaskTrigger) -> TaskStatus:
    """Trigger an example Celery task with a given sleep duration."""
    logger.info(
        f"Triggering example task with {task_in.seconds} seconds sleep")
    task = example_task.delay(task_in.seconds)
    return TaskStatus(task_id=task.id, status=task.status, result=task.result)


@router.get("/status/{task_id}", response_model=TaskStatus, summary="Get status of an async task")
async def get_task_status(task_id: str) -> TaskStatus:
    """Get the current status and result of a Celery task by ID."""
    task_result = AsyncResult(task_id)
    return TaskStatus(task_id=task_result.id, status=task_result.status, result=task_result.result)
