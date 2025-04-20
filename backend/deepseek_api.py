import requests
import json
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("OPENROUTER_API_KEY")
OPENROUTER_API_KEY = "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"

def get_deepseek_reply(messages: List) -> str:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": messages,
            }
        ),
    )
    return response.text
