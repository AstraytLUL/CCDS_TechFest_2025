from src import app, news_processor
from flask import request, jsonify, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    if data is None:
        return jsonify({'result': 'Invalid request: JSON data expected.'}), 415

    news_text = data.get('news_text', '')
    if not news_text.strip():
        return jsonify({'result': 'No news text provided.'}), 400
    
    # Process the input using Ollama
    result_message = news_processor.analyze_news_with_ollama(news_text)
    
    return jsonify({'result': result_message})
