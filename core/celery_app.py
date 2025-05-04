# Celery configuration for HAGAME Backend

import os
from celery import Celery

# Read Celery configuration from environment variables
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

celery_app = Celery(
    "hagame_tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["core.tasks"],  # Include task modules here
)

# Optional: Celery configuration dictionary
# celery_app.conf.update(
#     task_ignore_result=False,
#     task_track_started=True,
# )
