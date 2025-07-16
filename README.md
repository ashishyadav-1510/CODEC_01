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
### Output:
### Database:

## Video
## Explanation