from sqlalchemy.ext.asyncio import AsyncSession as _AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.ext.declarative import declarative_base as _declarative_base
from sqlalchemy.orm import sessionmaker as _sessionmaker

from config import DB_URL


engine = _create_async_engine(DB_URL)
Base = _declarative_base()
AsyncSession = _sessionmaker(  # pyright: ignore
    engine, class_=_AsyncSession, expire_on_commit=False  # pyright: ignore
)
