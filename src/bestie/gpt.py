from dataclasses import dataclass
from typing import TypeAlias

from openai import OpenAI
from openai._streaming import Stream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

from bestie.env import OPENAI_API_KEY

Response: TypeAlias = ChatCompletion | Stream[ChatCompletionChunk]


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
