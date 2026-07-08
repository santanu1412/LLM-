import os 
from pathlib import Path
try:
    try:
        from dotenv import load_dotenv
    except Exception:
        # dotenv may not be installed in some environments; provide a no-op
        def load_dotenv():
            return None
except Exception:
    # dotenv not available: define a no-op to avoid import errors in environments
    def load_dotenv():
        return None
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kha hai bhai")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt = "Do you know Santanu"

# 1. Define the messages variable dynamically using your prompt
messages = [
    {
        "role": role,
        "content": prompt
    }
]

# 2. Pass the messages variable to the correct parameter
response = client.chat.completions.create(
    model=model, 
    messages=messages
)

# Print the raw response object
print(response)
print("########################################")

# Extract and print just the model's text answer
answer = response.choices[0].message.content
print(answer)