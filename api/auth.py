from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreate, UserLogin, UserRead
from crud.user import get_user_by_email, create_user
from core.database import get_async_session
from core.auth import verify_password, create_access_token, get_current_user
from fastapi.responses import JSONResponse
from core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    response_description="The newly registered user's information.",
    responses={
        201: {
            "description": "User registered successfully.",
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
        400: {"description": "Email already registered."}
    }
)
async def register_user(user_in: UserCreate, session: AsyncSession = Depends(get_async_session)) -> UserRead:
    """
    Register a new user with a unique email and username.
    """
    logger.info(f"Registration attempt for email: {user_in.email}")
    existing = await get_user_by_email(session, user_in.email)
    if existing:
        logger.warning(
            f"Registration failed: Email already registered ({user_in.email})")
        raise HTTPException(
            status_code=400, detail="Email already registered.")
    user = await create_user(session, user_in)
    logger.info(f"User registered successfully: {user.email}")
    return UserRead.from_orm(user)


@router.post(
    "/login",
    summary="Authenticate user and return JWT",
    response_description="JWT access token and token type.",
    responses={
        200: {
            "description": "Login successful.",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "token_type": "bearer"
                    }
                }
            }
        },
        401: {"description": "Invalid credentials."}
    }
)
async def login_user(user_in: UserLogin, session: AsyncSession = Depends(get_async_session)):
    """
    Authenticate user with email and password. Returns a JWT access token if successful.
    """
    logger.info(f"Login attempt for email: {user_in.email}")
    user = await get_user_by_email(session, user_in.email)
    if not user or not verify_password(user_in.password, user.hashed_password):
        logger.warning(f"Login failed for email: {user_in.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    token_data = {"sub": str(user.id), "email": user.email}
    access_token = create_access_token(token_data)
    logger.info(f"Login successful for email: {user.email}")
    return {"access_token": access_token, "token_type": "bearer"}


@router.get(
    "/me",
    response_model=UserRead,
    summary="Get current authenticated user's info",
    response_description="The current user's information.",
    responses={
        200: {
            "description": "Current user info returned.",
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
async def get_me(current_user=Depends(get_current_user)):
    """
    Get the current authenticated user's information using the JWT access token.
    """
    logger.info(f"Get current user info: {current_user.email}")
    return UserRead.from_orm(current_user)
