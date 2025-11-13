def chatbot_reply(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"
    else:
        return "I'm not sure how to respond to that."

def main():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_reply(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break

# Run the chatbot
main()
