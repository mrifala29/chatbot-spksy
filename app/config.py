from pydantic_settings import BaseSettings

class LLMSettings(BaseSettings):
    llm_model: str
    llm_api_key: str
    llm_base_url: str
    llm_temperature: float
    llm_max_token: int

    class Config:
        env_file = ".env"

LLMSettings = LLMSettings()