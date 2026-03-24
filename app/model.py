import os

from langchain_openai import ChatOpenAI
from app.config import LLMSettings

def get_model():
    return ChatOpenAI(
        model=LLMSettings.llm_model,
        api_key=LLMSettings.llm_api_key,
        base_url=LLMSettings.llm_base_url,
        temperature=LLMSettings.llm_temperature,
        max_tokens=LLMSettings.llm_max_token,
    )