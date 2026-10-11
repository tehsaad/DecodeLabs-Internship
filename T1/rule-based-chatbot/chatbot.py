# Rule-Based AI Chatbot (Project 1)
# A simple terminal chatbot that answers using a dictionary of predefined responses.

# Knowledge base: each key is a user intent, each value is the bot's reply.
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Nice to meet you.",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I'm RuleBot, your rule-based chatbot.",
    "help": "You can greet me, ask my name, or ask how I am.",
    "thanks": "You're welcome!",
    "good morning": "Good morning! Have a wonderful day.",
}

# Commands that end the conversation.
exit_commands = ["exit", "quit", "bye"]

# Reply used when the input is not in the knowledge base.
fallback_message = "Sorry, I don't understand that."

# Welcome message shown once when the program starts.
print("RuleBot: Welcome! I'm RuleBot. Type 'help' to see what I can do.")
print("RuleBot: Type 'exit', 'quit', or 'bye' to end the chat.")

# Keep the chatbot running until the user enters an exit command.
while True:
    # Read the input, convert it to lowercase, and remove extra spaces.
    user_input = input("You: ").lower().strip()

    # Exit handling: say goodbye and stop the loop.
    if user_input in exit_commands:
        print("RuleBot: Goodbye! Have a great day.")
        break

    # Look up the reply; use the fallback message if the input is unknown.
    bot_response = responses.get(user_input, fallback_message)
    print("RuleBot:", bot_response)
