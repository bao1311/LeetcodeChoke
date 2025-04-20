from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from db import Problem, get_db

router = APIRouter()

class ProblemOut(BaseModel):
    problem_id: int
    rating: float
    title: str
    title_zh: Optional[str] = None
    title_slug: str
    contest_slug: str
    problem_index: str

    class Config:
        orm_mode = True

@router.get("/", response_model=List[ProblemOut])
async def list_problems(
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Problem)
    if min_rating is not None:
        stmt = stmt.where(Problem.rating >= min_rating)
    if max_rating is not None:
        stmt = stmt.where(Problem.rating <= max_rating)
    stmt = stmt.order_by(Problem.rating.desc())
    result = await db.execute(stmt)
    return result.scalars().all()

@router.get("/random", response_model=ProblemOut)
async def random_problem(
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Problem)
    if min_rating is not None:
        stmt = stmt.where(Problem.rating >= min_rating)
    if max_rating is not None:
        stmt = stmt.where(Problem.rating <= max_rating)
    stmt = stmt.order_by(func.random()).limit(1)
    result = await db.execute(stmt)
    problem = result.scalars().first()
    if not problem:
        raise HTTPException(status_code=404, detail="No problem found")
    return problem
