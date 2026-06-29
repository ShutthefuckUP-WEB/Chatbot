def normalize(message):
    result = ""
    prev = ""
    for ch in message:
        if ch != prev:
            result += ch
        prev = ch
    # Also collapse multiple spaces into one
    while "  " in result:
        result = result.replace("  ", " ")
    return result.strip()


# Function that returns a response based on the user's message
def get_response(message):
    # Normalize input (lowercase + collapse repeated letters)
    msg = normalize(message.lower())

    # Greetings
    if msg == "hi" or msg == "helo" or msg == "hey" or msg == "yo":
        return "Hello!"
    elif msg == "hello":
        return "Hi!"
    # How are you
    elif msg == "how are you" or msg == "how r u" or msg == "how are u":
        return "I'm fine, thanks! How about you?"
    # Identity questions
    elif msg == "what is your name" or msg == "what's your name" or msg == "your name":
        return "I'm a simple Python chatbot."
    elif msg == "who made you" or msg == "who created you":
        return "I was created using Python."
    # Thanks
    elif msg == "thank you" or msg == "thanks" or msg == "thx":
        return "You're welcome!"
    # Goodbyes (covers bye, byeee, see ya, see yaaa, goodbye, cya)
    elif msg == "bye" or msg == "goodbye" or msg == "se ya" or msg == "se you" or msg == "cya":
        return "Goodbye! Have a nice day!"
    else:
        # Fallback response for anything we don't recognise
        return "Sorry, I don't understand that."


# Helper: is this message a goodbye?
def is_goodbye(message):
    msg = normalize(message.lower())
    return msg == "bye" or msg == "goodbye" or msg == "se ya" or msg == "se you" or msg == "cya"


# Welcome message shown once when the program starts
print("Welcome to the Basic Python Chatbot!")
print("Type 'bye' to exit.\n")

# Keep chatting until the user says goodbye
while True:
    # Ask the user for input
    user_input = input("You: ")

    # Get the bot's reply from our function
    reply = get_response(user_input)

    # Show the bot's reply
    print("Bot:", reply)

    # Stop the loop when the user says bye (in any form)
    if is_goodbye(user_input):
        break

# Goodbye message after the loop ends
print("\nChat ended. Thanks for talking to me!")
