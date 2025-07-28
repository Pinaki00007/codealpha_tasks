def chatbot():
    print("🤖 Chatbot: Hello! Type something to begin (type 'exit' to end)\n")

    while True:
        user_input = input("👤 You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi there!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thank you! How can I help you?")
        elif user_input == "what is your name":
            print("🤖 Chatbot: I'm CodeAlphaBot, your Python assistant!")
        elif user_input == "who made you":
            print("🤖 Chatbot: I was created by a Python programmer.")
        elif user_input == "what can you do":
            print("🤖 Chatbot: I can chat with you and answer simple questions.")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
        elif user_input == "exit":
            print("🤖 Chatbot: Chat ended.")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Start chatbot
chatbot()
