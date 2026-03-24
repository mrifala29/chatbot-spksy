from pathlib import Path

def load_system_prompt() -> str:
    return Path("prompts/system_prompt.txt").read_text().strip()