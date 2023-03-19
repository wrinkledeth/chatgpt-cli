import os
from dotenv import load_dotenv
import openai
import pyperclip
import re

from pygments import highlight
from pygments.lexers import PythonLexer, get_lexer_by_name
from pygments.formatters import TerminalFormatter


def send_message(message, messages, role):
    """Send a message and append it to the messages list."""
    messages.append({"role": role, "content": message})


def main():
    """Start the chat application."""

    # Setup OpenAI API Client
    load_dotenv()
    openai.organization = os.getenv("OPENAI_ORGANIZATION")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    MODEL_ENGINE = "gpt-3.5-turbo"

    print(
        f"Welcome to {MODEL_ENGINE}!\n1. Type 'reset' to reset the chat, or 'messages' to see the messages.\n2. Multi-line inputs are supported. Type 'eom' in a new line to send your message.\n3. Replies are automatically copied to your clipboard.\n"
    )
    messages = []
    send_message("You are a helpful and kind AI Assistant.", messages, "system")
    show_prompt = True
    while True:
        prompt = ""
        while True:
            try:
                line = input("\033[31m>\033[0m " if show_prompt else "")
                show_prompt = False
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("Goodbye!")
                return
            if line == "eom":
                break
            if line == "reset":
                messages = []
                print("Chat reset!")
                send_message(
                    "You are a helpful and kind AI Assistant.", messages, "system"
                )
                show_prompt = True
                break
            if line == "messages":
                for message in messages:
                    print(message)
                show_prompt = True
                break
            prompt += line + "\n"
        prompt = prompt.strip()
        if prompt:
            send_message(prompt, messages, "user")
            chat = openai.ChatCompletion.create(model=MODEL_ENGINE, messages=messages)
            # reason = chat.choices[0].finish_reason
            # role = chat.choices[0].role
            reply = chat.choices[0].message.content
            pyperclip.copy(reply)  # automatically copy the AI's reply to clipboard
            fancy_print(reply)
            print("")
            send_message(reply, messages, "assistant")
            show_prompt = True


def fancy_print(markdown_str):
    """Highlight code blocks in a markdown string."""

    # use regex pattern to check for code block in markdown
    code_pattern = re.compile(r"```(\w*)\n(.+?)```", re.DOTALL)

    # highlight code blocks and print non-code parts
    for i, match in enumerate(code_pattern.finditer(markdown_str)):
        # print("Text before the code block #" + str(i + 1) + ":")
        print(markdown_str[: match.start()])
        # print("Highlighting code block #" + str(i + 1) + ":")
        lexer_alias = match.group(1)
        if not lexer_alias:
            print("(No lexer specified, using Python lexer)")
            lexer_alias = "python"
        lexer = get_lexer_by_name(lexer_alias, stripall=True)
        formatter = TerminalFormatter()
        code_block = match.group(2)
        print("(Start Code Block)")
        print(highlight(code_block, lexer, formatter))
        print("(End Code Block)")
        markdown_str = markdown_str[match.end() :]
    # print any remaining non-code text
    # print("Text after the last code block:")
    print(markdown_str)


if __name__ == "__main__":
    main()
