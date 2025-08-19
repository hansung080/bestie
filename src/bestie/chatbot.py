from bestie import gpt
from colorama import init, Fore, Style


class Chatbot:
    def __init__(self, model: str) -> None:
        self.model = model
        self.context = [{"role": "system", "content": "You are a helpful assistant."}]

    def add_user_message(self, message: str) -> None:
        self.context.append({"role": "user", "content": message})

    def send_request(self) -> gpt.Response:
        return gpt.client.chat.completions.create(
            model=self.model,
            messages=self.context,
        )

    def add_response(self, response: gpt.Response) -> None:
        message = response.choices[0].message
        self.context.append({"role": str(message.role), "content": str(message.content)})

    def get_last_message(self) -> str:
        return self.context[-1]["content"]


def run_cli():
    init(autoreset=True)
    print(f"Bestie> How can I help you? (Enter `{Fore.GREEN}exit{Style.RESET_ALL}` to quit chatting)")

    chatbot = Chatbot(gpt.model.gpt_4o_mini)
    while True:
        user_message = input(Fore.BLUE + "User> ")
        print(Style.RESET_ALL, end="")
        if user_message == "exit":
            break

        chatbot.add_user_message(user_message)
        response = chatbot.send_request()
        chatbot.add_response(response)
        print("Bestie> " + chatbot.get_last_message())


if __name__ == "__main__":
    run_cli()
