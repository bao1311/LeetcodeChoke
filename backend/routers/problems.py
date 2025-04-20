from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from db import Problem, get_db
from models import ProblemOut

router = APIRouter()

@router.get("/", response_model=List[ProblemOut])
async def list_problems(
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Problem)
    if min_rating is not None:
        stmt = stmt.where(Problem.rating >= min_rating)
    if max_rating is not None:
        stmt = stmt.where(Problem.rating <= max_rating)
    stmt = stmt.order_by(Problem.rating.desc())
    result = await db.execute(stmt)
    return result.scalars().all()
