from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OTUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
    
"""
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

print("👋👋 Welcome to the Chain of Thought Reasoning Demo! Please ask a question to see how the model breaks it down into smaller steps and explains its reasoning process.\n")

USER_PROMPT = input("👉👉 Please provide your prompt: ")

message_history.append({"role": "user", "content": USER_PROMPT})

while True:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=message_history,
        )

        raw_content = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_content})
        parsed_content = json.loads(raw_content)

        step = parsed_content.get("step")
        content = parsed_content.get("content", "")

        if step == "START":
            print(f"🔥🔥 Starting LLM reasoning process...\n{content}")
        elif step == "PLAN":
            print(f"🧠🧠 Planning the solution...\n{content}")
        elif step == "OUTPUT":
            print(f"✅✅ Final Answer:\n{content}")
            break
        else:
            print(f"Unknown step: {step}\n{content}")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        print(f"Raw response: {raw_content}")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break