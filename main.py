from chatbot import get_response
from database import log_interaction

print("Welcome to AI Chatbot!")
print("Enter Text\nType 'exit' to quit.\n")

# Continuous loop until user types 'exit'
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    bot_response = get_response(user_input)
    print("Bot:", bot_response)
    log_interaction(user_input, bot_response)
