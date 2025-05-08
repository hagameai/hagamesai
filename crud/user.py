import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from models.user import User
from schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext
from core.auth import get_password_hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    """Get a user by email."""
    result = await session.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def get_user_by_id(session: AsyncSession, user_id: uuid.UUID) -> User | None:
    """Get a user by id."""
    result = await session.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    """Create a new user with hashed password."""
    hashed_password = get_password_hash(user_in.password)
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(session: AsyncSession, user: User, user_in: UserUpdate) -> User:
    """Update user fields."""
    if user_in.username is not None:
        user.username = user_in.username
    if user_in.email is not None:
        user.email = user_in.email
    if user_in.password is not None:
        user.hashed_password = pwd_context.hash(user_in.password)
    await session.commit()
    await session.refresh(user)
    return user
