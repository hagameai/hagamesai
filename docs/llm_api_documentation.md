# LLM API Documentation

## Overview
This document provides detailed information about the LLM (Large Language Model) API endpoints available in the hagamesai project. The LLM API is designed to facilitate communication with the AI engine for various functionalities including natural language processing, cognitive modeling, and game interactions.

## Base URL
The base URL for all LLM API requests is:
```
http://<your-server-url>/api/llm
```

## Endpoints

### 1. Generate Text
- **Endpoint:** `/generate`
- **Method:** `POST`
- **Description:** Generates text based on the provided prompt.
- **Request Body:**
    - `prompt`: (string) The input text to generate a response from.
    - `max_length`: (integer) The maximum length of the generated response.

    Example:
    ```json
    {
        "prompt": "Once upon a time",
        "max_length": 100
    }
    ```
- **Response:**
    - `200 OK`
        ```json
        {
            "generated_text": "Once upon a time, in a land far away..."
        }
        ```
    - `400 Bad Request`
        ```json
        {
            "error": "Invalid input"
        }
        ```

### 2. Analyze Sentiment
- **Endpoint:** `/analyze/sentiment`
- **Method:** `POST`
- **Description:** Analyzes the sentiment of the provided text.
- **Request Body:**
    - `text`: (string) The input text for sentiment analysis.

    Example:
    ```json
    {
        "text": "I love playing games!"
    }
    ```
- **Response:**
    - `200 OK`
        ```json
        {
            "sentiment": "positive"
        }
        ```
    - `400 Bad Request`
        ```json
        {
            "error": "Invalid input"
        }
        ```

### 3. Cognitive Task
- **Endpoint:** `/cognitive/task`
- **Method:** `POST`
- **Description:** Executes a cognitive task based on the input data.
- **Request Body:**
    - `task_data`: (object) The data required to perform the cognitive task.

    Example:
    ```json
    {
        "task_data": {
            "question": "What is the capital of France?"
        }
    }
    ```
- **Response:**
    - `200 OK`
        ```json
        {
            "answer": "Paris"
        }
        ```
    - `400 Bad Request`
        ```json
        {
            "error": "Invalid input"
        }
        ```

## Error Handling
All error responses will include an error message indicating the nature of the issue. Ensure to handle error responses appropriately in client applications.

## Conclusion
This documentation serves as a comprehensive guide to the LLM API endpoints. For further details on implementation and usage, please refer to the source code and additional documentation available in the project.
