import nltk

nltk.download("punkt")

faq_responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Need any assistance?",
    "how are you": "I'm just a bot, but I'm functioning properly!",
    "what is your name": "I'm your AI Assistant!",
    "bye": "Goodbye! Have a nice day.",
    "default": "Sorry, I didn’t understand that.Try Something Else"
}

def preprocess(text):
    return text.lower().strip()

def get_response(user_input):
    user_input = preprocess(user_input)
    for key in faq_responses:
        if key in user_input:
            return faq_responses[key]
    return faq_responses["default"]
