# backend/routers/chat.py
from fastapi import APIRouter, Depends
from typing import List
from pydantic import BaseModel
from services.gemini_api import get_gemini_reply_manual

# 1) Define your request schema
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# 2) Create the router
router = APIRouter()

# 3) Mount your /chat endpoint on this router
@router.post("/", summary="Multi‑turn LeetCode chat")
async def chat(req: ChatRequest):
    reply = get_gemini_reply_manual(req.messages)
    return {"reply": reply}
