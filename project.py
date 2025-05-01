import random

def main():
    print("Hello! I'm your friendly chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Goodbye! Have a nice day.")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")

def get_response(user_input):
    """Generate a response based on user input."""
    if is_greeting(user_input):
        return random.choice(["Hello!", "Hi there!", "Hey, how can I help you?"])
    elif is_farewell(user_input):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])
    elif "how are you" in user_input:
        return random.choice([
            "I'm doing well, thank you!",
            "I'm great, how about you?",
            "Doing fine, how can I assist you?"
        ])
    elif "your name" in user_input:
        return "I am Chatbot, your virtual assistant!"
    elif "help" in user_input:
        return "I can chat with you, answer your basic questions, and more. Try asking about my name or how I'm doing!"
    else:
        return "Sorry, I didn't understand that. Can you ask something else?"

def is_greeting(user_input):
    greetings = ["hi", "hello", "hey", "howdy"]
    return any(greet in user_input for greet in greetings)

def is_farewell(user_input):
    farewells = ["bye", "goodbye", "see you", "take care"]
    return any(farewell in user_input for farewell in farewells)

if __name__ == "__main__":
    main()

