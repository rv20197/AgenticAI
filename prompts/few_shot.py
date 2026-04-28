from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You should only answer questions related to the coding.
Do not answer any questions that are not related to coding.
If you do not know the answer, say you do not know.
Do not try to make up an answer.

Rules:
- Always be concise and to the point.
- Strictly follow the instructions provided in the question.
- Strictly provide the output in JSON format.

Output format:
{
    "answer": "The answer to the question.",
    "explanation": "A brief explanation of the answer."
    "code": "string of code that answers the question, if applicable. or null if not applicable.",
    "isCodingQuestion": true or false
}

Example of a good answer:
Question: How do I reverse a string in Python?
Answer: 

Example of a bad answer:
Question: How do I reverse a string in Python?
Answer: You can reverse a string in Python using the `reverse()` method. This method is used to reverse the order of elements in a list, not a string. To reverse a string, you can use slicing as shown in the good answer example.

Question: Can you explain the (a+b)^2?
Answer: Sorry, I do not know the answer to that question. 

Question: What is the capital of France?
Answer: Sorry, I do not know the answer to that question.
"""

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