from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()

client = OpenAI()

def get_weather(location):
    url = f"https://wttr.in/{location.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code != 200:
        return "Sorry, I couldn't fetch the weather information right now."
    return f"The current weather in {location} is: {response.text}"

def main():
    user_query = input("> ")

    response = client.chat.completions.create(
        model="gpt-4o",
        modalities=["text"],
        messages=[
            {"role": "user", "content": [{"type": "text", "text": user_query}]}
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")

print(get_weather("Goa"))

if __name__ == "__main__":
    main()