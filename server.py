from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch
from flask import Flask, request, jsonify

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-distilled-squad')
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    context = data['context']
    question = data['question']
    
    # Tokenize input
    inputs = tokenizer(question, context, return_tensors='pt')
    
    # Get model output
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Process output to get answer
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end]))
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)