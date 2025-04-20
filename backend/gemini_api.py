# server.py

import os
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai.types import Content, Part, GenerateContentConfig
from fastapi import FastAPI
from models import ChatRequest
# from openai_client import get_chatgpt_response
from deepseek_api import get_deepseek_reply
from fastapi.middleware.cors import CORSMiddleware
from typing import List
load_dotenv()
# load your keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Define your Pydantic models
class Message(BaseModel):
    role: str     # "system" | "user" | "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# Create FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500"
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


# Instantiate once
client = genai.Client(api_key=GEMINI_API_KEY)

from google.genai.types import GenerateContentConfig

def get_gemini_reply_manual(messages: List[Message]) -> str:
    # 1️⃣ Extract just the raw text in order
    texts = [m.content for m in messages]

    # 2️⃣ Build a config that carries your system instruction + any other params
    cfg = GenerateContentConfig(
        system_instruction=[
            "You are a concise, helpful assistant. Reply in Markdown.",
            "You will be my Leetcode assistant today!",
            "You will only answer question about Data structure and Algorithms",
            "I will give you some rules to follow",
            "You will not spoil detailed solution for 30 mins",
            "In the first 5 minutes, you will not give me any hints at all when I solve a problem, you can only explain the problem statement in case it's too hard too understand",
            "After 10 minutes, you will give me the first high level hint if I ask",
            "After 15 minutes, you will give me the second hint",
            "After 30 minutes, you will be able to answer every question I have about the problem"
        ],
        max_output_tokens=300
    )

    # 3️⃣ Call Gemini with a list of strings
    resp = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=texts,
        config=cfg
    )
    return resp.text


@app.post("/chat")
async def chat(req: ChatRequest):
    reply = get_gemini_reply_manual(req.messages)
    return {"reply": reply}
