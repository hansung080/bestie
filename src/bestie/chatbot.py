from __future__ import annotations

from typing import Literal, TypedDict, cast

from colorama import Fore, Style, init as colorama_init

from bestie import gpt

type Response = gpt.Response


class Message(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


class Chatbot:
    def __init__(self, model: str) -> None:
        self.model: str = model
        self.messages: list[Message] = [{"role": "system", "content": "You are a helpful assistant."}]

    def add_user_message(self, content: str) -> None:
        self.messages.append({"role": "user", "content": content})

    def send_request(self) -> Response:
        return gpt.client.chat.completions.create(
            messages=cast(list[gpt.ChatCompletionMessageParam], self.messages),
            model=self.model,
        )

    def add_response(self, response: Response) -> None:
        message = response.choices[0].message
        assert message.role == "assistant"
        assert message.content is not None
        self.messages.append({"role": "assistant", "content": message.content})

    def get_last_message(self) -> str:
        return self.messages[-1]["content"]


def run_cli() -> None:
    colorama_init(autoreset=True)
    print(f"Bestie> How can I help you? (Enter `{Fore.GREEN}exit{Style.RESET_ALL}` to quit chatting)")

    chatbot = Chatbot(gpt.model.GPT_4O_MINI)
    while True:
        user_message = input(Fore.BLUE + "User> ").strip()
        print(Style.RESET_ALL, end="")
        if not user_message:
            continue
        elif user_message == "exit":
            break

        chatbot.add_user_message(user_message)
        response = chatbot.send_request()
        chatbot.add_response(response)
        print("Bestie> " + chatbot.get_last_message())


if __name__ == "__main__":
    run_cli()
