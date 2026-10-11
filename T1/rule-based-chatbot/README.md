# Rule-Based AI Chatbot

## Project Overview

RuleBot is a simple terminal chatbot written in Python. It does not use machine
learning. Instead, it follows fixed rules: it looks up what the user typed in a
dictionary of predefined responses and prints the matching reply. If it does not
recognize the input, it prints a fallback message.

## Features

- **Continuous conversation:** runs inside a `while True:` loop until the user exits.
- **Input sanitization:** `.lower().strip()` makes input case-insensitive and removes extra spaces, so `"  HELLO  "` is treated as `"hello"`.
- **Dictionary knowledge base:** the replies are stored in a dictionary named `responses`, with 8 intents.
- **Dictionary lookup:** replies are found with `responses.get()`, with no `if-elif` chain.
- **Fallback response:** unknown input gets `"Sorry, I don't understand that."`
- **Greeting handling:** recognizes `hello`, `hi`, and `hey`.
- **Exit handling:** `exit`, `quit`, or `bye` prints a farewell and stops the loop with `break`.

### Supported Intents

| You type            | RuleBot replies                                   |
|---------------------|---------------------------------------------------|
| `hello`             | Hello! How can I help you?                        |
| `hi`                | Hi there! Nice to meet you.                       |
| `hey`               | Hey! What can I do for you?                       |
| `how are you`       | I'm doing great! Thanks for asking.               |
| `what is your name` | I'm RuleBot, your rule-based chatbot.             |
| `help`              | You can greet me, ask my name, or ask how I am.   |
| `thanks`            | You're welcome!                                   |
| `good morning`      | Good morning! Have a wonderful day.               |
| `exit` / `quit` / `bye` | Goodbye! Have a great day. *(ends the chat)*  |

## Prerequisites

- Python 3.x installed (no external libraries required)

## How to Run

Open a terminal in the `rule-based-chatbot` folder and run:

```bash
python chatbot.py
```

> On some systems (Linux/macOS) the command is `python3 chatbot.py`.

## Example Conversation

```text
RuleBot: Welcome! I'm RuleBot. Type 'help' to see what I can do.
RuleBot: Type 'exit', 'quit', or 'bye' to end the chat.
You: Hello
RuleBot: Hello! How can I help you?
You:    WHAT IS YOUR NAME
RuleBot: I'm RuleBot, your rule-based chatbot.
You: how are you
RuleBot: I'm doing great! Thanks for asking.
You: what's the weather?
RuleBot: Sorry, I don't understand that.
You: thanks
RuleBot: You're welcome!
You: bye
RuleBot: Goodbye! Have a great day.
```

## How the Dictionary `.get()` Method Works

A dictionary stores **key-value pairs**. In this project, the key is what the user
types and the value is the bot's reply:

```python
responses = {
    "hello": "Hello! How can I help you?",
    "thanks": "You're welcome!",
}
```

The `.get()` method takes two arguments:

```python
responses.get(key, default)
```

1. **`key`**: the value to look up (the user's sanitized input).
2. **`default`**: what to return if the key is **not** in the dictionary.

```python
responses.get("hello", "Sorry, I don't understand that.")
# -> "Hello! How can I help you?"

responses.get("weather", "Sorry, I don't understand that.")
# -> "Sorry, I don't understand that."
```

### Why use `.get()` instead of `responses[key]` or `if-elif`?

- `responses[key]` crashes with a `KeyError` when the key does not exist. `.get()` returns the default instead.
- An `if-elif` chain gets longer with every new intent. With a dictionary, adding an intent is one new line in `responses`, and the lookup code does not change.
- The fallback is built into a single line of code.

## Project Structure

```text
rule-based-chatbot/
├── chatbot.py   # The complete chatbot program
└── README.md    # Project documentation
```
