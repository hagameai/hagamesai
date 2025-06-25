# AI Engine Integration Guide

This document provides a comprehensive guide for integrating AI engine services into your applications using the hagamesai backend. 

## Overview
The AI engine services are designed to provide advanced functionalities for human-vs-AI gameplay, leveraging large language models (LLMs) and cognitive modeling. This guide will help you understand how to utilize these services effectively.

## Prerequisites
Before you begin integration, ensure that you have the following:
- Access to the hagamesai backend API.
- An understanding of FastAPI endpoints.
- Required libraries and dependencies installed, including `httpx` for API requests.

## Integration Steps

### 1. Setting Up Your Environment
Ensure your development environment is configured. You can use a virtual environment to maintain project dependencies.

```bash
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Install required packages
pip install httpx
```

### 2. Making API Requests to the AI Engine
Use the following example to make requests to the AI engine service endpoints:

```python
import httpx

async def call_ai_engine(prompt: str):
    url = "http://localhost:8000/api/llm"
    payload = {'prompt': prompt}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()
```

### 3. Handling Responses
The AI engine will return a JSON response. You should handle this response appropriately:

```python
response_data = await call_ai_engine("Hello AI, how can you assist me today?")
if response_data['success']:
    print("AI Response:", response_data['data'])
else:
    print("Error:", response_data['error'])
```

### 4. Error Handling
Implement error handling to manage potential issues during the API call:

```python
async def call_ai_engine(prompt: str):
    url = "http://localhost:8000/api/llm"
    payload = {'prompt': prompt}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        return {'success': False, 'error': str(e)}
    except Exception as e:
        print("An error occurred:", str(e))
        return {'success': False, 'error': str(e)}
```

## Conclusion
This guide provides a starting point for integrating AI engine services with your application. Ensure you adapt the integration to your specific use case and error handling needs. For further details, refer to the API documentation.

## Additional Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [HTTPX Documentation](https://www.python-httpx.org/)

---
This guide is part of the hagamesai project documentation, which aims to support developers in building innovative AI-powered applications.