import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatgpt_response(user_input: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4.1",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant for LeetCode problems."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message["content"]
