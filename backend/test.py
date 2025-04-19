import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "deepseek/deepseek-chat-v3-0324:free",
    "messages": [
      {
        "role": "user",
        "content": "Can you explain how to solve two-sum problem for?"
      }
    ],
    
  })

)

# Print raw response if debugging
print("Status:", response.status_code)
print("Raw:", response.text)

# Parse and print actual AI reply
if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("AI says:", reply)
else:
    print("Error:", response.json())