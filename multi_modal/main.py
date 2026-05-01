from openai import  OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[{
        "role": "user",
        "content":[
            {
                "type": "text",
                "text": "Generate a caption for this image in about 20 words."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://images.pexels.com/photos/12902857/pexels-photo-12902857.jpeg"
                }
            }
        ]
    }]
)

print(response.choices[0].message.content)