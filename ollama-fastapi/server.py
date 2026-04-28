from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434"
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
async def read_contact_us():
    return {"message": "Contact us at contact@example.com"}

@app.post("/chat")
async def chat(messages: str = Body(..., description="The messages for the chat")):
    response = client.chat(
        model="gemma2:2b",
        messages=[{"role": "user", "content": messages}]
    )
    return {"response": response.message.content}