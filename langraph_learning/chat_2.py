import re
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Literal, Optional
from openai import OpenAI
from langgraph.graph import StateGraph,START,END

load_dotenv()

client = OpenAI()

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional [bool]

def chatbot(state: State):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {
                "role": "user",
                "content": state.get("user_query")
            }
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: State) ->  Literal["chatbot_gemini", "end_node"]:
    # Evaluate the chatbot response and only route to the Gemini model if the response appears incorrect.
    user_query = state.get("user_query", "") or ""
    llm_output = state.get("llm_output", "") or ""

    if not llm_output.strip():
        state["is_good"] = False
        return "chatbot_gemini"

    is_good = False
    math_match = re.search(r"(\d+(?:\s*[\+\-\*\/]\s*\d+)+)", user_query)
    if math_match:
        try:
            expected = eval(math_match.group(1))
            is_good = str(expected) in llm_output
        except Exception:
            is_good = False
    else:
        # If no simple math expression is found, consider the response good if the model returned non-empty text.
        is_good = bool(llm_output.strip())

    state["is_good"] = is_good
    return "end_node" if is_good else "chatbot_gemini"

def chatbot_gemini(state: State):
    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {
                "role": "user",
                "content": state.get("user_query")
            }
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def end_node(state: State):
    return state


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("evaluate_response", evaluate_response)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("end_node", end_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini", "end_node")
graph_builder.add_edge("end_node", END)

compiledGraph = graph_builder.compile()

updatedState = compiledGraph.invoke(State({"user_query": "Hey, What is 2 * 56"}))

print(updatedState)