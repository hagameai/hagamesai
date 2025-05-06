from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserRead, UserUpdate
from schemas.cognitive_profile import CognitiveProfileRead, CognitiveProfileUpdate
from crud.user import update_user
from crud.cognitive_profile import get_by_user_id, create_profile, update_profile
from core.database import get_async_session
from core.auth import get_current_user
from core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/users/me", tags=["users"])


@router.get(
    "/profile",
    response_model=UserRead,
    summary="Get current user's profile info",
    response_description="The current user's profile information.",
    responses={
        200: {
            "description": "Current user profile info returned.",
            "content": {
                "application/json": {
                    "example": {
                        "id": "b3b7c7e2-1c2d-4e2a-8e2b-1c2d4e2a8e2b",
                        "username": "testuser",
                        "email": "test@example.com",
                        "created_at": "2024-06-01T12:00:00Z",
                        "updated_at": "2024-06-01T12:00:00Z"
                    }
                }
            }
        },
        401: {"description": "Not authenticated."}
    }
)
async def get_profile(current_user=Depends(get_current_user)):
    """
    Get the current user's profile information using the JWT access token.
    """
    logger.info(f"Profile access for user: {current_user.email}")
    return UserRead.from_orm(current_user)


@router.put(
    "/profile",
    response_model=UserRead,
    summary="Update current user's profile info",
    response_description="The updated user's profile information.",
    responses={
        200: {
            "description": "User profile updated successfully.",
            "content": {
                "application/json": {
                    "example": {
                        "id": "b3b7c7e2-1c2d-4e2a-8e2b-1c2d4e2a8e2b",
                        "username": "updateduser",
                        "email": "updated@example.com",
                        "created_at": "2024-06-01T12:00:00Z",
                        "updated_at": "2024-06-02T12:00:00Z"
                    }
                }
            }
        },
        400: {"description": "Invalid update data."},
        401: {"description": "Not authenticated."}
    }
)
async def update_profile_info(
    user_update: UserUpdate,
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """
    Update the current user's profile information. Only provided fields will be updated.
    """
    logger.info(f"Profile update attempt for user: {current_user.email}")
    user = await update_user(session, current_user, user_update)
    logger.info(f"Profile updated for user: {user.email}")
    return UserRead.from_orm(user)


@router.get(
    "/cognitive-profile",
    response_model=CognitiveProfileRead,
    summary="Get current user's cognitive profile",
    response_description="The current user's cognitive profile information.",
    responses={
        200: {
            "description": "Current user cognitive profile info returned.",
            "content": {
                "application/json": {
                    "example": {
                        "id": "c7e2b3b7-1c2d-4e2a-8e2b-1c2d4e2a8e2b",
                        "user_id": "b3b7c7e2-1c2d-4e2a-8e2b-1c2d4e2a8e2b",
                        "profile_data": {"risk_aversion": 0.7, "decision_speed": "fast"},
                        "last_updated": "2024-06-01T12:00:00Z"
                    }
                }
            }
        },
        401: {"description": "Not authenticated."},
        404: {"description": "Cognitive profile not found."}
    }
)
async def get_cognitive_profile(
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """
    Get the current user's cognitive profile. Returns 404 if not found.
    """
    logger.info(f"Cognitive profile access for user: {current_user.email}")
    profile = await get_by_user_id(session, current_user.id)
    if not profile:
        logger.warning(
            f"Cognitive profile not found for user: {current_user.email}")
        raise HTTPException(
            status_code=404, detail="Cognitive profile not found.")
    return CognitiveProfileRead.from_orm(profile)


@router.put(
    "/cognitive-profile",
    response_model=CognitiveProfileRead,
    summary="Update or create current user's cognitive profile",
    response_description="The updated or newly created cognitive profile information.",
    responses={
        200: {
            "description": "Cognitive profile updated or created successfully.",
            "content": {
                "application/json": {
                    "example": {
                        "id": "c7e2b3b7-1c2d-4e2a-8e2b-1c2d4e2a8e2b",
                        "user_id": "b3b7c7e2-1c2d-4e2a-8e2b-1c2d4e2a8e2b",
                        "profile_data": {"risk_aversion": 0.8, "decision_speed": "slow"},
                        "last_updated": "2024-06-02T12:00:00Z"
                    }
                }
            }
        },
        400: {"description": "Invalid update data."},
        401: {"description": "Not authenticated."}
    }
)
async def update_cognitive_profile(
    update_in: CognitiveProfileUpdate,
    current_user=Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """
    Update or create the current user's cognitive profile. If no profile exists, a new one will be created.
    """
    logger.info(
        f"Cognitive profile update attempt for user: {current_user.email}")
    profile = await get_by_user_id(session, current_user.id)
    if profile:
        profile = await update_profile(session, profile, update_in)
        logger.info(
            f"Cognitive profile updated for user: {current_user.email}")
    else:
        profile = await create_profile(session, current_user.id, update_in.profile_data)
        logger.info(
            f"Cognitive profile created for user: {current_user.email}")
    return CognitiveProfileRead.from_orm(profile)
