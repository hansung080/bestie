from __future__ import annotations

from dataclasses import dataclass

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam

from bestie.env import OPENAI_API_KEY

__all__ = [
    "ChatCompletionMessageParam",
    "Model",
    "OpenAI",
    "Response",
    "client",
    "model",
]

# type Response = ChatCompletion | Stream[ChatCompletionChunk]  # openai._streaming.Stream not supported
type Response = ChatCompletion


@dataclass(frozen=True)
class Model:
    GPT_4O: str = "gpt-4o-2024-05-13"
    GPT_4O_MINI: str = "gpt-4o-mini-2024-07-18"


model: Model = Model()

client: OpenAI = OpenAI(
    api_key=OPENAI_API_KEY,
    timeout=30,
    max_retries=1,
)
