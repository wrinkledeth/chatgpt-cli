# ChatGPT CLI Tool

## .env

```bash
➜ cat .env          
OPENAI_API_KEY=***
OPENAI_ORGANIZATION=*** 
```

## Usage

```text
➜ python chat.py
Welcome to gpt-3.5-turbo! Type 'reset' to reset the chat, or 'messages' to see the messages.

> tell me a super funny joke
Why don't scientists trust atoms? Because they make up everything!
---
> now turn it into a super meta and deep haiku
Tiny particles,  
Atoms form life's very core,  
Yet, mistrust rules all.
---
> what did we just talk about?
We talked about a funny joke and then I turned it into a haiku for you.
---
> messages
{'role': 'system', 'content': 'You are a helpful and kind AI Assistant.'}
{'role': 'user', 'content': 'tell me a super funny joke'}
{'role': 'system', 'content': "Why don't scientists trust atoms? Because they make up everything!"}
{'role': 'user', 'content': 'now turn it into a super meta and deep haiku'}
{'role': 'system', 'content': "Tiny particles,  \nAtoms form life's very core,  \nYet, mistrust rules all."}
{'role': 'user', 'content': 'what did we just talk about?'}
{'role': 'system', 'content': 'We talked about a funny joke and then I turned it into a haiku for you.'}
> reset
Chat reset!
> messages
{'role': 'system', 'content': 'You are a helpful and kind AI Assistant.'}
> what did we just talk about?
We haven't talked about anything yet. How may I assist you today?
---
> 
```
