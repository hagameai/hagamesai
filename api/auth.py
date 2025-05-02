from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreate, UserLogin, UserRead
from crud.user import get_user_by_email, create_user
from core.database import get_async_session
from core.auth import verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate, session: AsyncSession = Depends(get_async_session)) -> UserRead:
    """Register a new user."""
    existing = await get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(
            status_code=400, detail="Email already registered.")
    user = await create_user(session, user_in)
    return UserRead.from_orm(user)


@router.post("/login")
async def login_user(user_in: UserLogin, session: AsyncSession = Depends(get_async_session)):
    """Authenticate user and return JWT."""
    user = await get_user_by_email(session, user_in.email)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    token_data = {"sub": str(user.id), "email": user.email}
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserRead)
async def get_me(current_user=Depends(get_current_user)):
    """Get the current authenticated user's info."""
    return UserRead.from_orm(current_user)
