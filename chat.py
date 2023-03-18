import os
from dotenv import load_dotenv
import openai
import json

# from colorama import init, Fore, Style

load_dotenv()  # load environmental variables from .env file
openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"


def main():
    print(
        f"Welcome to {model_engine}! Type 'reset' to reset the chat, or 'messages' to see the messages.\n"
    )
    messages = []
    prefix = {"role": "system", "content": "You are a helpful and kind AI Assistant."}
    messages.append(prefix)
    while True:
        prompt = input("\033[31m>\033[0m ")
        if prompt == "reset":
            messages = []
            messages.append(prefix)
            print("Chat reset!")
            continue
        if prompt == "messages":
            for message in messages:
                print(message)
            continue

        messages.append({"role": "user", "content": prompt})
        chat = openai.ChatCompletion.create(model=model_engine, messages=messages)
        reply = chat.choices[0].message.content
        print(f"{reply}\n---")
        messages.append({"role": "system", "content": reply})


if __name__ == "__main__":
    main()
