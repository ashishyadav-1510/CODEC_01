# AI Chatbot with SQLite Logging

A simple, rule-based Python chatbot that provides responses to frequently asked questions and logs all user-bot interactions into a SQLite database.

## Features

* ✅ Predefined FAQ-based chatbot responses
* ✅ Input preprocessing (case and space normalization)
* ✅ Default response for unknown queries
* ✅ Conversation logging using **SQLite**
* ✅ Timestamped chat history
* ✅ Easy to extend with more FAQs

## Technologies Used

* **Python 3**
* **NLTK** for tokenization
* **SQLite3** for database logging

## Project Structure

chatbot_project/
│
├── chatbot.py        # Contains chatbot logic and response system
├── database.py       # Handles SQLite logging (initialization and insertion)
├── main.py           # Runs the chatbot interface and logs interactions
├── chatlog.db        # SQLite database file (auto-generated)
└── README.md         # Project documentation (this file)

## ▶️ How to Run

1. **Install Python 3** (if not already installed)
2. **Install NLTK** :

pip install nltk

1. **Download tokenizer** :

import nltk
nltk.download('punkt')

1. **Run the chatbot** :

python main.py

## Sample Conversation

Welcome to AI Chatbot!
Enter Text
Type 'exit' to quit.

You: Hello
Bot: Hi there! How can I help you today?

You: What is your name?
Bot: I'm your AI Assistant!

You: bye
Bot: Goodbye! Have a nice day.

## Sample FAQ Responses

| User Input        | Bot Response                                          |
| ----------------- | ----------------------------------------------------- |
| hello / hi        | Hi there! / Hello! Need any assistance?               |
| how are you       | I'm just a bot, but I'm functioning properly!         |
| what is your name | I'm your AI Assistant!                                |
| bye               | Goodbye! Have a nice day.                             |
| anything else     | Sorry, I didn’t understand that. Try something else. |

## Database Schema (`chatlog`)

| Field        | Type     | Description                |
| ------------ | -------- | -------------------------- |
| id           | INTEGER  | Auto-increment primary key |
| user_input   | TEXT     | User's input               |
| bot_response | TEXT     | Bot's response             |
| timestamp    | DATETIME | Auto-generated timestamp   |


## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101900.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101910.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101926.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20104539.png?raw=true)

### Output:
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20102009.png?raw=true)
### Database:
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20102044.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20102055.png?raw=true)

## Video

[Video on YouTube]()

## Explanation

✅ Part 1: FAQ Chatbot Logic (chatbot.py)

import nltk
This imports the NLTK (Natural Language Toolkit) library, commonly used for natural language processing (NLP) tasks.

nltk.download("punkt")
Downloads the "punkt" tokenizer model, which is used for breaking text into sentences or words. Required for some advanced NLP but not strictly used in this current code (included for future use).

📚 FAQ Responses

faq_responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Need any assistance?",
    "how are you": "I'm just a bot, but I'm functioning properly!",
    "what is your name": "I'm your AI Assistant!",
    "bye": "Goodbye! Have a nice day.",
    "default": "Sorry, I didn’t understand that.Try Something Else"
}
A dictionary (faq_responses) that maps known user queries (keys) to bot responses (values).
"default" is used as a fallback when the user input does not match any known question.

✂️ Preprocess Function

def preprocess(text):                                                                                                                                                    
    return text.lower().strip()
This function cleans up user input before matching it:
text.lower() converts all text to lowercase (so "Hello" matches "hello").
.strip() removes any leading/trailing whitespace.
Helps ensure consistent matching.

🧠 Response Function

def get_response(user_input):
    user_input = preprocess(user_input)
    for key in faq_responses:
        if key in user_input:
            return faq_responses[key]
    return faq_responses["default"]
get_response() takes the user's message and tries to find a suitable reply.
user_input = preprocess(user_input) — cleans the input using the preprocess function.
for key in faq_responses: — loop over all known keywords in the FAQ dictionary.
if key in user_input: — check if any keyword is a substring of the user input.
If a match is found, it returns the mapped response.
If no keyword is found, it returns the "default" response.

✅ Part 2: Database Logic (database.py)

import sqlite3
Imports Python’s built-in SQLite database module to work with .db files (used for local storage).

🏗️ Create Database Table

def init_db():
    conn = sqlite3.connect("chatlog.db")  # Connect to (or create) the database file
    cursor = conn.cursor()  # Create a cursor to execute SQL commands
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chatlog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)  # SQL command to create a table with 4 columns
    conn.commit()  # Save changes
    conn.close()   # Close database connection
Creates a table called chatlog if it doesn't already exist.
Table columns:
id: Auto-incrementing primary key.
user_input: The user's input.
bot_response: The response from the bot.
timestamp: Auto-generated current date and time.

📥 Insert Chat into Database

def log_interaction(user_input, bot_response):
    conn = sqlite3.connect("chatlog.db")  # Connect to database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chatlog (user_input, bot_response) VALUES (?, ?)",
                   (user_input, bot_response))  # Insert values using placeholders
    conn.commit()  # Save changes
    conn.close()   # Close connection
Saves a conversation into the database by inserting user input and bot response.
Uses ? placeholders to prevent SQL injection.

📌 Initialize DB on Import

init_db()
Calls the init_db() function when this module is imported, so the database and table are ready before use.

✅ Part 3: Main Program (main.py)

from chatbot import get_response
from database import log_interaction
Imports the chatbot logic and logging function from other files (chatbot.py, database.py).

🖥️ User Interface

print("Welcome to AI Chatbot!")
print("Enter Text\nType 'exit' to quit.\n")
Greets the user and explains how to exit the chat.

🔁 Main Chat Loop

while True:
    user_input = input("You: ")
Continuously prompts the user for input.

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
If the user types "exit", the loop breaks, and the bot says goodbye.

    bot_response = get_response(user_input)
    print("Bot:", bot_response)
    log_interaction(user_input, bot_response)
Calls get_response() to generate a reply.
Displays the bot's response.
Calls log_interaction() to save the interaction to the database.

