import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.cognitive_profile import CognitiveProfile
from schemas.cognitive_profile import CognitiveProfileUpdate


async def get_by_user_id(session: AsyncSession, user_id: uuid.UUID) -> CognitiveProfile | None:
    """Get cognitive profile by user_id."""
    result = await session.execute(select(CognitiveProfile).where(CognitiveProfile.user_id == user_id))
    return result.scalars().first()


async def create_profile(session: AsyncSession, user_id: uuid.UUID, profile_data: dict) -> CognitiveProfile:
    """Create a new cognitive profile for a user."""
    profile = CognitiveProfile(user_id=user_id, profile_data=profile_data)
    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile


async def update_profile(session: AsyncSession, profile: CognitiveProfile, update_in: CognitiveProfileUpdate) -> CognitiveProfile:
    """Update cognitive profile data."""
    profile.profile_data = update_in.profile_data
    await session.commit()
    await session.refresh(profile)
    return profile
