import nltk
from nltk.tokenize import word_tokenize

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How can I assist you?",
    "how are you": "I am fine. What about you?",
    "what is your name": "I am an AI Chatbot built using NLP.",
    "bye": "Goodbye! Have a nice day."
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        tokens = word_tokenize(user_input)

        found = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", responses[key])
                found = True
                break

        if not found:
            print("Chatbot: Sorry, I did not understand that.")

        if "bye" in user_input:
            break

chatbot()