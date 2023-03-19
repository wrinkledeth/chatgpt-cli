# ChatGPT CLI Tool

## Links

[openai platform](https://platform.openai.com/)
[org settings](https://platform.openai.com/account/org-settings)
[api reference](https://platform.openai.com/docs/api-reference)
[api usage](https://platform.openai.com/account/usage)

## .env

```bash
➜ cat .env          
OPENAI_API_KEY=***
OPENAI_ORGANIZATION=*** 
```

## Usage

```text
python chat.py
Welcome to gpt-3.5-turbo!
1. Type 'reset' to reset the chat, or 'messages' to see the messages.
2. Multi-line inputs are supported. Type 'eom' in a new line to send your message.
3. Replies are automatically copied to your clipboard.

> tell me a joke
eom
Sure, here's a joke for you:
Why did the tomato turn red?
Because it saw the salad dressing!

> turn it into a haiku
eom
Tomato turns red,
Dressing seen and it blushes,
Salad now complete.

> what did we just talk about?
eom
You asked me to tell you a joke, and I shared a tomato joke with you. You then asked me to turn the joke into a haiku, which I did.

> messages
{'role': 'system', 'content': 'You are a helpful and kind AI Assistant.'}
{'role': 'user', 'content': 'tell me a joke'}
{'role': 'assistant', 'content': "Sure, here's a joke for you:\n\nWhy did the tomato turn red?\n\nBecause it saw the salad dressing!"}
{'role': 'user', 'content': 'turn it into a haiku'}
{'role': 'assistant', 'content': 'Tomato turns red,\nDressing seen and it blushes,\nSalad now complete.'}
{'role': 'user', 'content': 'what did we just talk about?'}
{'role': 'assistant', 'content': 'You asked me to tell you a joke, and I shared a tomato joke with you. You then asked me to turn the joke into a haiku, which I did.'}
> reset
Chat reset!
> messages
{'role': 'system', 'content': 'You are a helpful and kind AI Assistant.'}
> what did we just talk about
eom
We have not had any previous conversation before this current one. If you are referring to our current conversation, we have not discussed anything significant yet. How may I be of assistance to you?
```
