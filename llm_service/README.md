# LLM Service Overview

The LLM (Large Language Model) Service is a crucial component of the hagamesai project, enabling advanced AI capabilities to facilitate human-vs-AI gameplay. This service provides endpoints that allow for interactions with the LLM, handling requests and responses efficiently.

## Purpose
The LLM Service is designed to:
- Provide a seamless interface for integrating LLM functionalities into game scenarios.
- Support various cognitive tasks such as conversation, problem-solving, and decision-making.
- Offer robust processing capabilities to handle multiple user requests simultaneously.

## Usage Instructions
To utilize the LLM Service, ensure that the service is running and follow the steps below:

### 1. Setup
Make sure to install the required dependencies. If you are using a virtual environment, activate it and run:
```bash
pip install -r requirements.txt
```

### 2. Running the Service
You can start the LLM Service by running the following command in your terminal:
```bash
uvicorn llm_service.service:app --host 0.0.0.0 --port 8000
```

### 3. API Endpoints
The LLM Service exposes several API endpoints that you can use to interact with the model:

- **POST /llm/request**: This endpoint allows you to send a request to the LLM.
  - **Request Body**:
    ```json
    {
      "prompt": "Your input text here",
      "parameters": {
        "max_tokens": 100,
        "temperature": 0.7
      }
    }
    ```
  - **Response**:
    ```json
    {
      "response": "Generated response from LLM"
    }
    ```

### 4. Example Request
Here is an example of how to make a request to the LLM endpoint using `curl`:
```bash
curl -X POST "http://localhost:8000/llm/request" -H "Content-Type: application/json" -d '{"prompt":"What is the capital of France?","parameters":{"max_tokens":10}}'
```

## Conclusion
This LLM Service is a key building block for enhancing gameplay experiences in hagamesai by leveraging advanced AI technologies. For further integration details and examples, please refer to the API documentation.

## License
This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.