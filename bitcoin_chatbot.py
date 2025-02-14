import random

responses = {
    "hello": "Hi! How can I help you with Bitcoin?",
    "what is bitcoin": "Bitcoin is a decentralized digital currency.",
    "who created bitcoin": "Bitcoin was created by an unknown person using the alias Satoshi Nakamoto.",
    "how does mining work": "Bitcoin mining is a process where powerful computers solve cryptographic puzzles to secure the network.",
    "bye": "Goodbye! Keep learning about Bitcoin!"
}

def bitcoin_chatbot():
    print("🤖 Bitcoin Chatbot: Ask me anything about Bitcoin!")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print(f"🤖: {responses[user_input]}")
        elif "bye" in user_input:
            print("🤖: Goodbye!")
            break
        else:
            print("🤖: I'm still learning! Try asking something else.")

bitcoin_chatbot()
