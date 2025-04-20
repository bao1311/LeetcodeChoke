from fastapi import FastAPI
from models import ChatRequest
# from openai_client import get_chatgpt_response
from deepseek_api import get_deepseek_reply
from fastapi.middleware.cors import CORSMiddleware
from gemini_api import get_gemini_reply
from typing import List

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

@app.post("/chat")
async def chat(req: ChatRequest):
    response = get_gemini_reply(req.messages)
    return {"reply": response}

@app.get("/")
async def root():
    return {"Message": "Welcome to Leetchoke API"}