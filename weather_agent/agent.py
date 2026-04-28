from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import cast, Optional
import requests
import json
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_current_weather(location):
    url = f"https://wttr.in/{location.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code != 200:
        return "Sorry, I couldn't fetch the weather information right now."
    return f"The current weather in {location} is: {response.text}"

def run_command(cmd: str):
    result = os.system(cmd)
    return result

available_tools = {
    "get_current_weather": get_current_weather,
    "run_command": run_command
}

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also use TOOL step if you want to use any external tool to resolve the query.
    For every TOOL step, you need to first check if you have the tool available for the task you want to perform.
    For every Tool Call wait for the observe step which is going to have the output of the tool you called.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL" , "content": "string" }

    Available Tools:
    1. get_current_weather(location: str) -> str : This tool takes a location as input and returns the current weather information for that location.
    2. run_command(cmd: str) -> str : This tool takes a system command as input and executes it on the user's system, returning the output from that command.

    Example 1:
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

    Example 2:
    START: Hey, What is the current weather in Goa?
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in weather information" }
    PLAN: { "step": "PLAN": "content": "Let's see if we have the tool for fetching weather information" }
    PLAN: { "step": "PLAN": "content": "Great! I have the tool for fetching weather information named get_current_weather" }
    PLAN: { "step": "PLAN": "content": "Now I need to use the tool get_current_weather with location as Goa" }
    TOOL: { "step": "TOOL": "TOOL":"get_current_weather", "input": "Goa" }
    TOOL: { "step": "OBSERVE": "TOOL":"get_current_weather", "output": "The current weather in Goa is: Partly cloudy, 25°C" }
    PLAN: { "step": "PLAN": "content": "Great, I have received the output of the tool get_current_weather for Goa" }
    OUTPUT: { "step": "OUTPUT": "content": "The current weather in Goa is: Partly cloudy, 25°C" }
    
"""

class My_output_format(BaseModel):
    step: str = Field(..., description="The ID of the step. The step can be START, PLAN, TOOL or OUTPUT, etc.")
    content: Optional[str] = Field(None, description="The optional string content for the step.")
    tool: Optional[str] = Field(None, description="The ID of the tool to be called in case of TOOL step.")
    input: Optional[str] = Field(None, description="The input to be given to the tool in case of TOOL step.")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

print("👋👋 Welcome to the weather assistant.\n")

while True:
    USER_PROMPT = input("👉👉 Please provide your prompt: ")

    message_history.append({"role": "user", "content": USER_PROMPT})

    while True:
        raw_content = ""
        try:
            response = client.chat.completions.parse(
                model="gemini-3-flash-preview",
                response_format=My_output_format,
                messages=cast(list[ChatCompletionMessageParam], message_history),
            )

            raw_content = response.choices[0].message.content
            if raw_content is None:
                print("Error: No content in response")
                break
            message_history.append({"role": "assistant", "content": raw_content})
            parsed_content = response.choices[0].message.parsed
            if parsed_content is None:
                parsed_content = json.loads(raw_content)
            
            step = parsed_content.get("step") if isinstance(parsed_content, dict) else parsed_content.step
            content = parsed_content.get("content") if isinstance(parsed_content, dict) else parsed_content.content

            if step == "START":
                print(f"🔥🔥 {content}")
            elif step == "TOOL":
                # Handle different formats of TOOL content
                content = parsed_content.get("content") if isinstance(parsed_content, dict) else parsed_content.content
                tool_name = parsed_content.get("TOOL") if isinstance(parsed_content, dict) else getattr(parsed_content, 'tool', None)
                tool_input = parsed_content.get("input") if isinstance(parsed_content, dict) else getattr(parsed_content, 'input', None)

                if not tool_name:
                    if isinstance(content, str):
                        if content.startswith('TOOL: '):
                            tool_name = content.split('TOOL: ')[1].strip()
                        else:
                            try:
                                # Try to parse content as JSON
                                tool_data = json.loads(content)
                                tool_name = tool_data.get('TOOL')
                                tool_input = tool_data.get('input') or tool_input
                            except json.JSONDecodeError:
                                pass  # tool_name remains None
                    elif isinstance(content, dict):
                        tool_name = content.get('TOOL')
                        tool_input = content.get('input') or tool_input
                
                print(f"🔧🔧 Calling tool: {tool_name} with input: {tool_input}")
                if tool_name in available_tools:
                    tool_output = available_tools[tool_name](tool_input)
                    message_history.append({"role": "developer", "content": json.dumps({"step": "OBSERVE", "tool": tool_name, "output": tool_output})})
                else:
                    print(f"❌❌ Unknown tool: {tool_name}")
                continue
            elif step == "PLAN":
                print(f"🧠🧠 {content}")
            elif step == "OUTPUT":
                print(f"🤖🤖 Final Answer:\n{content}")
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