import requests

def analyze_news_with_ollama(news_text):
    # Construct your prompt, including instructions as needed.
    prompt = (
        "Analyze the following news article for signs of misinformation. "
        "Explain why it might be false and provide a link to a trusted source "
        "for verification. If you do not think this is any type of misinformation, justify your thoughts\n\n"
        f"News Article: {news_text}"
    )
    
    # Specify your Ollama API endpoint
    api_url = "http://127.0.0.1:11434"
    
    # Create the payload with the prompt and the model identifier
    payload = {
        "prompt": prompt,
        "model": "deepseek-r1:8b",
        # Optionally, you can include other parameters like temperature or max tokens if supported
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.ok:
        result = response.json()
        # Adjust parsing according to your API response structure
        return result.get("response", "No response key found")
    else:
        return f"Error: {response.status_code} - {response.text}"