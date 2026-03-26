from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from alempie.config import settings

# CRITIEK: De URL moet beginnen met 'postgresql+asyncpg://' 
# of 'sqlite+aiosqlite://'
url = settings.SQLALCHEMY_DATABASE_URI

# Gebruik create_async_engine in plaats van create_engine
engine = create_async_engine(
    url, 
    echo=True,
    future=True
)

# We maken een 'factory' voor async sessies
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Asynchrone dependency die een AsyncSession levert.
    """
    async with async_session_maker() as session:
        yield session