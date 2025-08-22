import os

from dataclasses import dataclass
from typing import TypeAlias

from dotenv import load_dotenv

from openai import OpenAI
from openai._streaming import Stream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk


Response: TypeAlias = ChatCompletion | Stream[ChatCompletionChunk]


@dataclass(frozen=True)
class Model:
    gpt_4o: str = "gpt-4o-2024-05-13"
    gpt_4o_mini: str = "gpt-4o-mini-2024-07-18"


model = Model()

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=30,
    max_retries=1,
)
