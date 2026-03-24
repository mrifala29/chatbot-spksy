from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from app.schema import ChatResponse


def build_agent(model, checkpointer):
    return create_agent(
        model=model,
        checkpointer=checkpointer,
        # tools=[],
        response_format=ToolStrategy(ChatResponse),
    )