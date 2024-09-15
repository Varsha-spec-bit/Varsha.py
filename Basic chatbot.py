# Install NLTK if not already installed
# !pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

# Define the conversation pairs
pairs = [
    # Greetings
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you today?"]],
    ["good morning", ["Good morning! How can I help you today?"]],
    ["good evening", ["Good evening! How can I assist you today?"]],
    
    # Asking the bot's name
    ["(.*) your name?", ["I am your friendly chatbot.", "My name is Chatbot, nice to meet you!"]],
    
    # How are you? conversation
    ["how are you?", ["I'm just a computer program, but I'm doing well! How about you?"]],
    ["how (.*) you?", ["I'm doing great, thank you! How can I assist you today?"]],
    
    # Questions about the weather
    ["(.*) weather (.*)", ["I don't have access to live weather data, but I recommend checking a weather website."]],
    
    # Asking for the bot's capabilities
    ["what can you do?|what are your skills?|how can you help me?", 
     ["I can chat with you, answer basic questions, and provide information on various topics."]],
    
    # Gratitude
    ["thank you|thanks", ["You're welcome!", "Glad I could help!"]],
    
    # Asking about time
    ["what time is it?", ["Sorry, I can't tell the time, but you can check a clock nearby!"]],
    
    # Default responses for unrecognized input
    ["(.*)", [
        "Sorry, I don't quite understand that. Could you please rephrase?",
        "Hmm, I'm not sure about that. Could you ask something else?",
        "I'm not equipped to handle that. Maybe try asking in a different way?"
    ]],
]

# Create the chatbot using NLTK's built-in Chat class
chatbot = Chat(pairs, reflections)

# Start the chatbot conversation
def start_nltk_chatbot():
    print("Hello, I'm your chatbot. Type 'quit' to exit the chat.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Call the function to initiate the chatbot
start_nltk_chatbot()
