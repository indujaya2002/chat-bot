import random

# Define a function to get a greeting response
def greet_response(user_message):
    greetings = ["hi", "hello", "hey", "hola"]
    for word in user_message.split():
        if word.lower() in greetings:
            return "Hello! How can I assist you today?"
    return None

# Define a function to get a response to a user's question
def question_response(user_message):
    user_message = user_message.lower()
    if "who are you" in user_message:
        return "I am a chatbot. What can I do for you?"
    elif "how are you" in user_message:
        return "I'm just a computer program, but thanks for asking!"
    elif "what can you do" in user_message:
        return "I can answer questions, provide information, or just chat with you."
    return None

# Define a function to handle user input
def chatbot_response(user_message):
    responses = []
    
    # Check for greetings
    greeting_response = greet_response(user_message)
    if greeting_response:
        responses.append(greeting_response)

    # Check for questions
    question_response = question_response(user_message)
    if question_response:
        responses.append(question_response)

    if not responses:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"
    
    return random.choice(responses)

# Main loop for chatbot
print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
