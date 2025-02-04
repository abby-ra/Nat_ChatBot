import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]),
    (r"how are you?", ["I'm good, how about you?", "Doing well!"]),
    (r"how it's going", ["It's going well!"]),
    (r"What's your fav color?", ["White"]),
    (r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]),
    (r"quit", ["Goodbye!", "See you later!"])
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
print("Chatbot: Hi! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")
