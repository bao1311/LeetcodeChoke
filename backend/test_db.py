# test_db.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DATABASE_URL = "postgresql+asyncpg://leetuser:1311@localhost:5432/leetcode"

print('DATABASE_URL',DATABASE_URL)
async def test_conn():
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        # wrap your SQL string in text()
        result = await conn.execute(text("SELECT 1"))
        print(result.scalar_one())  # should print: 1
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_conn())
