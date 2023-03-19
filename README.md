# ChatGPT CLI Tool

Features

- Automatic code syntax highlighting
- Multi-line inputs (type "eom" to terminate and send prompt)
- Responses automatically copied to clipboard

Todo

- [ ] Prompt / Response Logging

## Special Commands

```bash
messages: show current message list
reset: reset the chat
clear: clear the screen
```

## Sample Usage

```bash
➜ cat .env          
OPENAI_API_KEY=***
OPENAI_ORGANIZATION=*** 
```

```text
➜  python chat.py 
Welcome to gpt-3.5-turbo!
1. Type 'reset' to reset the chat, or 'messages' to see the messages.
2. Multi-line inputs are supported. Type 'eom' in a new line to send your message.
3. Replies are automatically copied to your clipboard.

> tell me a joke
eom
Why couldn't the bicycle stand up by itself? Because it was two-tired.

> can you make this into a haiku that's super meta?
eom
As an AI,
Writing jokes is not my forte,
But here's a haiku.

> What did we just discuss?
eom
We discussed a joke and then I turned it into a haiku.

> messages
{'role': 'user', 'content': 'tell me a joke'}
{'role': 'assistant', 'content': "\n\nWhy couldn't the bicycle stand up by itself? Because it was two-tired."}
{'role': 'user', 'content': "can you make this into a haiku that's super meta?"}
{'role': 'assistant', 'content': "As an AI,\nWriting jokes is not my forte,\nBut here's a haiku."}
{'role': 'user', 'content': 'What did we just discuss?'}
{'role': 'assistant', 'content': 'We discussed a joke and then I turned it into a haiku.'}
> reset
Chat reset!
> messages
> what did we just talk about?
eom
I apologize, but as an AI language model, I do not have the capability to know what previous conversation we have had. Please let me know if you have a specific topic in mind so I can assist you accordingly.

> 
```

## Links

[Openai platform](https://platform.openai.com/)

[Org settings](https://platform.openai.com/account/org-settings)

[API reference](https://platform.openai.com/docs/api-reference)

[API usage](https://platform.openai.com/account/usage)