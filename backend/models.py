from pydantic import BaseModel
from typing import List, Dict


class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

from typing import Optional
from pydantic import BaseModel

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
