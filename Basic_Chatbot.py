
#Simple rule based chatbot
def chatbot_response(user_input):
    user_input=user_input.lower() #make input lowercase for consistency

    if user_input=="hello":
        return "Hi"
    elif user_input=="how are you":
        return "I'm fine, Thanks!"
    elif user_input=="bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("Chatbot:Hello! type 'bye' to exit ")
    while True:
        user_input=input("You: ")
        response=chatbot_response(user_input)
        print("Chatbot: ",response)
        if user_input.lower()== "bye":
            break

#run chatbot
run_chatbot()