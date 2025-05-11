from pydantic import BaseModel


class TaskTrigger(BaseModel):
    """Schema for triggering an example task."""
    seconds: int


class TaskStatus(BaseModel):
    """Schema for returning task status."""
    task_id: str
    status: str
    result: str | None = None
