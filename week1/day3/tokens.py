import os 
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    # dotenv may not be installed in some environments; provide a no-op
    def load_dotenv():
        return None

from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kha hai bhai")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt1 = "Hii"
prompt2 = "Explain Time travel in detail"
prompt3 = "Write a 100 word essay on machine learning"

prompts= [prompt1, prompt2, prompt3]

for prompt in prompts:
    message={
        "role": role,
        "content": prompt
    }
    message = [message]
# 1. Define the messages as a single, flat list of dictionaries
messages = [
    {
        "role": "system",
        "content": "you are a world class Hacker Teacher, who guide me to study about eathical hancing and  how to protect our nation from Cyber crimes"
    },
    {
        "role": role,
        "content": prompt
    }
]

# 2. Pass the messages variable to the API
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