# Usage Examples for LLM Service Endpoints

This document provides examples of how to use the LLM (Large Language Model) service endpoints exposed by the API. The LLM service is designed to facilitate interactions with advanced AI functionalities, including text generation, summarization, and more.

## Endpoint: Generate Text

### Request
To generate text using the LLM service, send a POST request to the following endpoint:

```http
POST /api/llm/generate
```

### Sample Request Body
```json
{
  "prompt": "Once upon a time in a distant galaxy...",
  "max_tokens": 150,
  "temperature": 0.7
}
```

### Example using Python's `requests` library
```python
import requests

url = "http://localhost:8000/api/llm/generate"
headers = {"Content-Type": "application/json"}

payload = {
    "prompt": "Once upon a time in a distant galaxy...",
    "max_tokens": 150,
    "temperature": 0.7
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    result = response.json()
    print("Generated Text:", result['text'])
else:
    print("Error:", response.status_code, response.text)
```

## Endpoint: Summarize Text

### Request
To summarize a given text, send a POST request to:

```http
POST /api/llm/summarize
```

### Sample Request Body
```json
{
  "text": "The quick brown fox jumps over the lazy dog. This sentence is often used as a pangram in English, demonstrating the usage of every letter in the alphabet.",
  "max_tokens": 50
}
```

### Example using Python's `requests` library
```python
import requests

url = "http://localhost:8000/api/llm/summarize"
headers = {"Content-Type": "application/json"}

payload = {
    "text": "The quick brown fox jumps over the lazy dog. This sentence is often used as a pangram in English, demonstrating the usage of every letter in the alphabet.",
    "max_tokens": 50
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    result = response.json()
    print("Summary:", result['summary'])
else:
    print("Error:", response.status_code, response.text)
```

## Conclusion
These examples demonstrate how to effectively interact with the LLM service endpoints. Ensure that the API is running and accessible at the specified URL before making requests. Adjust the `max_tokens` and `temperature` parameters as needed to tailor the output to your specific requirements.