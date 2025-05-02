import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings
from typing import AsyncGenerator


class Settings(BaseSettings):
    """Settings for database configuration."""
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency that provides an async database session."""
    async with AsyncSessionLocal() as session:
        yield session
