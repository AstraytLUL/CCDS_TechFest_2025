import requests
from ollama import chat, ChatResponse

def analyze_news_with_ollama(news_text):
    # Construct your prompt, including instructions as needed.
    prompt = (
        "Analyze the following news article for signs of misinformation. " +
        "Explain why it might be false and provide a link to a trusted source " +
        "for verification. If you do not think this is any type of misinformation, justify your thoughts\n\n" +
        f"News Article: {news_text}"
    )
    
    response: ChatResponse = chat(model='llama3.2:latest', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])


    
    return response.message.content