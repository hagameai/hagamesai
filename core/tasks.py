# Define Celery tasks here

from core.celery_app import celery_app
import time
import logging

logger = logging.getLogger(__name__)


@celery_app.task
def example_task(seconds: int):
    """An example Celery task that sleeps for a specified number of seconds."""
    logger.info(f"Starting example task, sleeping for {seconds} seconds...")
    time.sleep(seconds)
    logger.info("Example task finished.")
    return f"Slept for {seconds} seconds"
