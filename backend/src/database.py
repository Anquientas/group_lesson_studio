# from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    # AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Model(DeclarativeBase):
    pass


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_factory() as session:
#         yield session


async_engine = create_async_engine(
    url=settings.DATABASE_TEST_URL,
    echo=True
)

new_async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)
