# Basic Chatbot in Python
# A beginner-friendly, rule-based chatbot.
# Uses only built-in Python: functions, if-elif-else, while loop, input(), print().

# Function that returns a response based on the user's message
def get_response(message):
    # Check the message against predefined rules
    if message == "hello":
        return "Hi!"
    elif message == "hi":
        return "Hello!"
    elif message == "how are you":
        return "I'm fine, thanks! How about you?"
    elif message == "what is your name":
        return "I'm a simple Python chatbot."
    elif message == "who made you":
        return "I was created using Python."
    elif message == "thank you":
        return "You're welcome!"
    elif message == "bye":
        return "Goodbye! Have a nice day!"
    else:
        # Fallback response for anything we don't recognise
        return "Sorry, I don't understand that."


# Welcome message shown once when the program starts
print("Welcome to the Basic Python Chatbot!")
print("Type 'bye' to exit.\n")

# Keep chatting until the user types "bye"
while True:
    # Ask the user for input
    user_input = input("You: ")

    # Convert to lowercase so capitalisation doesn't matter
    user_input = user_input.lower()

    # Get the bot's reply from our function
    reply = get_response(user_input)

    # Show the bot's reply
    print("Bot:", reply)

    # Stop the loop when the user says bye
    if user_input == "bye":
        break

# Goodbye message after the loop ends
print("\nChat ended. Thanks for talking to me!")
