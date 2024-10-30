import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

def get_chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    print("Welcome to the AI-Powered Chatbot!")
    print("Type 'exit' to quit the chat.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break
        
        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

if _name_ == "_main_":
    main()