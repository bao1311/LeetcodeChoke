from fastapi import FastAPI
from models import ChatRequest
# from openai_client import get_chatgpt_response
from deepseek_api import get_deepseek_reply

app = FastAPI()

@app.post("/chat")
async def chat(req: ChatRequest):
    response = get_deepseek_reply(req.messages)
    return {"reply": response}