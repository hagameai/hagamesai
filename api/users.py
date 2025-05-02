from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserRead, UserUpdate
from schemas.cognitive_profile import CognitiveProfileRead, CognitiveProfileUpdate
from crud.user import update_user
from crud.cognitive_profile import get_by_user_id, create_profile, update_profile
from core.database import get_async_session
from core.auth import get_current_user

router = APIRouter(prefix="/users/me", tags=["users"])


@router.get("/profile", response_model=UserRead)
async def get_profile(current_user=Depends(get_current_user)):
    """Get the current user's profile info."""
    return UserRead.from_orm(current_user)


@router.put("/profile", response_model=UserRead)
async def update_profile_info(
    user_update: UserUpdate,
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Update the current user's profile info."""
    user = await update_user(session, current_user, user_update)
    return UserRead.from_orm(user)


@router.get("/cognitive-profile", response_model=CognitiveProfileRead)
async def get_cognitive_profile(
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Get the current user's cognitive profile."""
    profile = await get_by_user_id(session, current_user.id)
    if not profile:
        raise HTTPException(
            status_code=404, detail="Cognitive profile not found.")
    return CognitiveProfileRead.from_orm(profile)


@router.put("/cognitive-profile", response_model=CognitiveProfileRead)
async def update_cognitive_profile(
    update_in: CognitiveProfileUpdate,
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Update or create the current user's cognitive profile."""
    profile = await get_by_user_id(session, current_user.id)
    if profile:
        profile = await update_profile(session, profile, update_in)
    else:
        profile = await create_profile(session, current_user.id, update_in.profile_data)
    return CognitiveProfileRead.from_orm(profile)
