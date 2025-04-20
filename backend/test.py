from google import genai
from google.genai.types import GenerateContentConfig

# 1️⃣ Create your client
client = genai.Client(api_key="AIzaSyBeTl4HCRIpDHAQjH9oa_8m-o9ljl76BNo")

# 2️⃣ Define your system instructions
system_instr = [
    "You are a concise, helpful assistant.",
    "Use Markdown formatting for code snippets."
]

# 3️⃣ Start a chat session with those instructions
chat = client.chats.create(
    model="gemini-2.0-flash-001",
    config=GenerateContentConfig(system_instruction=system_instr)
)

# 4️⃣ Send your first user message
resp = chat.send_message("Hi Gemini! Can you give me a quick Python example for reading a CSV?")
print(resp.text)

# 5️⃣ Continue the conversation seamlessly
resp = chat.send_message("Now show me how to filter rows where `age > 30`.")
print(resp.text)
