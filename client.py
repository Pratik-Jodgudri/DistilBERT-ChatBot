import requests

def chat():
    print("Welcome to the DistilBERT Chatbot!")
    print("Type 'quit' to exit.")
    
    while True:
        question = input("You: ")
        if question.lower() == 'quit':
            break
        
        context = input("Please provide some context: ")
        
        try:
            response = requests.post('http://localhost:5000/ask', 
                                     json={'question': question, 'context': context},
                                     timeout=30)
            
            if response.status_code == 200:
                print("Bot:", response.json()['answer'])
            else:
                print(f"Sorry, I couldn't process your request. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    choice = input("Enter 'chat' to start chatting: ")
    if choice.lower() == 'chat':
        chat()
    else:
        print("Invalid choice. Exiting.")