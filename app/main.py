from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

from app.schema import ChatRequest, ChatResponse
from app.model import get_llm
from app.memory import get_memory

app = FastAPI(title="Speakeasy AI Chatbot")


def load_system_prompt():
    with open("prompts/system_prompt.txt") as f:
        return f.read()


SYSTEM_PROMPT = load_system_prompt()


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    memory = get_memory(req.session_id)

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ])

    chain = LLMChain(
        llm=get_llm(),
        prompt=prompt,
        memory=memory
    )

    result = chain.invoke({
        "input": req.message
    })

    return ChatResponse(response=result["text"])