from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,MessagesState,START, END
from langchain.chat_models import init_chat_model
load_dotenv()

llm = init_chat_model(model="gpt-5.2", model_provider="openai")


class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot (state: MessagesState):
    response = llm.invoke(state.get("messages", []))
    return {"messages": [{"role":"ai","content":response.content}]}

def sample_node(state: MessagesState):
    return {"messages": [{"role":"ai","content":"Hi, This is a message from a sample node\n"}]}

graph_builder = StateGraph(State)

graph_builder.add_node(chatbot)
graph_builder.add_node(sample_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample_node")
graph_builder.add_edge("sample_node", END)
graph_builder = graph_builder.compile()

updated_state = graph_builder.invoke(State({"messages":[
    {
        "role":"user",
        "content": "Hi!, My name is Vatsal\n"
    }
]}))

print(f"\n\nUpdated state: {updated_state.get('messages')}")