from fastapi import FastAPI
from app.model import get_model
from app.memory import get_checkpointer
from app.agent import build_agent
from app.schema import ChatRequest, ChatResponse
from app.prompts import load_system_prompt

app = FastAPI()

agent = build_agent(
    model=get_model(),
    checkpointer=get_checkpointer(),
)


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    config = {"configurable": {"thread_id": request.session_id}}

    response = agent.invoke(
        {
            "messages": [
                {"role": "system", "content": load_system_prompt()},
                {"role": "user", "content": request.message},
            ]
        },
        config=config,
    )

    return response["structured_response"]