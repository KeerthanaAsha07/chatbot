print("=== Simple Chatbot ===")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "your name":
        print("Bot: I am a Python chatbot.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
