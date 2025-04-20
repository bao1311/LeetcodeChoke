from pydantic import BaseModel
from typing import List, Dict


class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
