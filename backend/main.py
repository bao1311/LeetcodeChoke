from fastapi import FastAPI
from models import ChatRequest
# from openai_client import get_chatgpt_response
# from deepseek_api import get_deepseek_reply
from fastapi.middleware.cors import CORSMiddleware
from services.gemini_api import get_gemini_reply_manual
from typing import List
from routers.chat import router as chat_router
from routers.problems import router as problems_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
app.include_router(chat_router,     prefix="/chat", tags=["chat"])
app.include_router(problems_router, prefix="/problems", tags=["problems"])

@app.post("/chat")
async def chat(req: ChatRequest):
    response = get_gemini_reply_manual(req.messages)
    return {"reply": response}

@app.get("/")
async def root():
    return {"Message": "Welcome to Leetchoke API"}