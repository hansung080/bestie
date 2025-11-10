import os

from dotenv import load_dotenv


def getenv_or_raise(key: str) -> str:
    if (value := os.getenv(key)) is None:
        raise EnvironmentError(f"environment variable '{key}' required")
    return value


load_dotenv()

OPENAI_API_KEY: str = getenv_or_raise("BESTIE_OPENAI_API_KEY")
