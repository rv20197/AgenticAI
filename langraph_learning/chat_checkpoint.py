from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(model="gpt-5.2", model_provider="openai")
DB_URI = "mongodb://root:example@localhost:27017"
COLLECTION_NAME = "chat_checkpoint"

config = {"configurable": {"thread_id": "1"}}


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm.invoke(state.get("messages", []))
    return {"messages": [{"role": "ai", "content": response.content}]}


def compile_graph_with_checkpoint(
    graph_builder: StateGraph, checkpointer: MongoDBSaver
):
    return graph_builder.compile(checkpointer=checkpointer)


graph_builder = StateGraph(State)

graph_builder.add_node(chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_memory = compile_graph_with_checkpoint(graph_builder, checkpointer)
    for chunk in graph_with_memory.stream(
        State({"messages": [{"role": "user", "content": "What am I learning?\n"}]}),
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

