# DistilBERT Chatbot

This project implements a simple question-answering chatbot using the DistilBERT model. It consists of a server that runs the DistilBERT model and a client that interacts with the server.

## Features

- Uses DistilBERT model for question answering
- Flask-based server for handling requests
- Simple command-line client interface
- Includes a test function to verify the chatbot's functionality

## Requirements

- Python 3.7+
- Flask
- PyTorch
- Transformers
- Requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/distilbert-chatbot.git
   cd distilbert-chatbot
   ```

2. Install the required packages:
   ```
   pip install flask torch transformers requests
   ```

## Usage

### Starting the Server

1. Open a terminal and navigate to the project directory.
2. Run the server:
   ```
   python server.py
   ```
3. The server will start and listen on `http://localhost:5000`.

### Running the Client

1. Open another terminal and navigate to the project directory.
2. Run the client:
   ```
   python client.py
   ```
3. Choose whether you want to chat or run a test:
   - Enter 'chat' to start the chat interface
   - Enter 'test' to run the test function

### Chatting with the Bot

1. When prompted, enter your question.
2. Provide some context for the question when asked.
3. The bot will respond with an answer based on the given context.
4. Type 'quit' to exit the chat.

## Files

- `server.py`: Contains the Flask server and DistilBERT model implementation.
- `client.py`: Implements the chat interface and test function.

## Note

- The first run of the server might take some time as it downloads the DistilBERT model.
- Ensure you have sufficient RAM available, as the model can be memory-intensive.
- If you encounter CUDA or GPU-related issues, you may need to use a CPU-only version of PyTorch.

## Contributing

Contributions to improve the chatbot are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
