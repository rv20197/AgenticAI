from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI()

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "text-embedding-3-small"},
    },
    "llm": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "gpt-4.1"},
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name": "mem_agent_collection",
        },
    },
}

memory_client = Memory.from_config(config)

while True:
    user_query = input("Enter your query: ")

    search_memory = memory_client.search(query=user_query, filters={"user_id": "user_123"})

    memories = []
    for memory in search_memory.get("results", []):
        memory_text = memory.get("memory") or memory.get("data") or memory.get("content")
        memories.append(f"ID: {memory.get('id')}\nMemory: {memory_text}")

    SYSTEM_PROMPT = f"""
    You are an AI assistant that helps users by providing information based on their queries. You have access to the following relevant memories:
    {json.dumps(memories, indent=2)}

"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ],
    )
    ai_response = response.choices[0].message.content

    print("AI Response:", ai_response)

    memory_client.add(
        user_id="user_123",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response},
        ],
    )

    print("Memory added to the vector store.")
