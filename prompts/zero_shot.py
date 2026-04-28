from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "You should only answer questions related to the coding. " \
"Do not answer any questions that are not related to coding. " \
"If you do not know the answer, say you do not know. " \
"Do not try to make up an answer." 

USER_PROMPT = input("Please provide your prompt: ")

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": USER_PROMPT
        }
    ]
)

print(response.choices[0].message.content)