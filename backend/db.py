# db.py
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, Numeric, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from .env
load_dotenv()

# Database URL, fallback to local default
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://leetuser:secret123@localhost:5432/leetcode"
)

# 1️⃣ Create the async SQLAlchemy engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,                   # True for SQL echo, can disable in prod
)

# 2️⃣ Create a session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False       # prevents attributes from refreshing after commit
)

# 3️⃣ Base class for ORM models
Base = declarative_base()

# 4️⃣ ORM model for the `problems` table
class Problem(Base):
    __tablename__ = "problems"

    rating        = Column(Numeric, nullable=False)
    problem_id    = Column(Integer, primary_key=True, index=True)
    title         = Column(Text, nullable=False)
    title_zh      = Column(Text)
    title_slug    = Column(Text, nullable=False)
    contest_slug  = Column(Text)
    problem_index = Column(Text)

# 5️⃣ FastAPI dependency
async def get_db():
    """
    Yield an AsyncSession, and ensure it’s closed after use.
    """
    async with AsyncSessionLocal() as session:
        yield session
