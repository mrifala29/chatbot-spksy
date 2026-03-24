from pathlib import Path

def load_system_prompt() -> str:
    return Path("app/prompts/system_prompt.txt").read_text().strip()