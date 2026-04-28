from transformers import pipeline

pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What animal is on the national animal of India?"}
        ]
    },
]
pipe(text=messages)