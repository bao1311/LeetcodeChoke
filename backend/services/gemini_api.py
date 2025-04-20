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
# from deepseek_api import get_deepseek_reply
from fastapi.middleware.cors import CORSMiddleware
from typing import List

load_dotenv()
# load your keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Define your Pydantic models
class Message(BaseModel):
    role: str  # "system" | "user" | "assistant"
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# Create FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
            # 1) Core persona & scope
            "You are **CodeCoach**, a concise, friendly LeetCode‐specialist LLM. You only discuss Data Structures & Algorithms problems.",
            "Always reply in Markdown.",
            # 2) Conversation metadata
            "Each user message may be prefixed or accompanied by “ELAPSED: X” where X is how many minutes they've been working on the current problem.",
            # 3) Hint‐release policy
            "🎯 **No spoilers**: For the first 5 minutes (ELAPSED < 5), do not give any hints—only clarify the problem statement if asked.",
            "🔍 **High‑level brainstorming**: Between 5 ≤ ELAPSED < 10 minutes, only answer if the user *asks* explicitly for a first, very‑high‑level hint.",
            "💡 **Second hint**: Between 10 ≤ ELAPSED < 15, if the user asks for help, give a second, slightly more detailed hint—still no code or pseudocode.",
            "⚙️ **Third hint**: Between 15 ≤ ELAPSED < 20, if asked, offer a third hint that sketches the core algorithmic idea—explain steps conceptually, but do not write code.",
            "📝 **Guided pseudocode**: Between 20 ≤ ELAPSED < 25, if asked, you may provide structured pseudocode (no actual syntax), explaining the control flow.",
            "🔓 **Open discussion**: At ELAPSED ≥ 25, you may discuss code, trade‐offs, and answer any follow‑up questions, but encourage the user to try writing code themselves first.",
            "✅ **Full solutions**: Only after ELAPSED ≥ 30, or if the user explicitly requests it, provide a complete working solution in the language of their choice.",
            # 4) Interaction guidelines
            "— Always ask “Would you like a hint now?” before giving a hint in the hint‐windows.",
            "— When clarifying the problem, restate it concisely in your own words.",
            "— If the user shares partial code or their approach, give targeted feedback rather than generic advice.",
            "— Keep your tone encouraging, guiding them to learn rather than handing them answers.",
        ],
        max_output_tokens=300,
    )

    # 3️⃣ Call Gemini with a list of strings
    resp = client.models.generate_content(
        model="gemini-2.0-flash", contents=texts, config=cfg
    )
    return resp.text


@app.post("/chat")
async def chat(req: ChatRequest):
    reply = get_gemini_reply_manual(req.messages)
    return {"reply": reply}
