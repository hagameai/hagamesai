# LLM Service Integration Documentation

## Overview
The LLM (Large Language Model) service provides advanced AI capabilities for human-vs-AI gameplay within the hagamesai application. This documentation outlines the integration points, usage, and configuration of the LLM service, which is built using FastAPI.

## Features
- **AI-Powered Gameplay**: Leverages LLMs to create intelligent behaviors in non-playable characters (NPCs).
- **Cognitive Modeling**: Supports advanced decision-making processes and cognitive profiles for game entities.

## Integration Points
The LLM service is integrated through the following components:

- **API Endpoints**: LLM service exposes several API endpoints that can be consumed by the frontend or other services.
- **Background Tasks**: Utilizes Celery for asynchronous processing of LLM requests and responses.

## Configuration
To configure the LLM service, ensure that the following environment variables are set:

| Environment Variable | Description |
|----------------------|-------------|
| `LLM_SERVICE_URL`   | The URL of the LLM service endpoint. |
| `LLM_API_KEY`       | API key for authenticating requests to the LLM service. |

## Usage
### API Endpoints
The LLM service provides the following endpoints:

1. **Generate Response**  
   `POST /api/llm/generate`  
   - **Request Body**:  
     ```json
     {
       "input": "string"
     }
     ```  
   - **Response**:  
     ```json
     {
       "output": "string"
     }
     ```  
   - **Description**: This endpoint generates a response based on the provided input string.

### Background Tasks
The processing of requests to the LLM service is handled asynchronously. Ensure that your Celery workers are running to process LLM tasks.

## Error Handling
The LLM service implements standard error handling. Common HTTP status codes include:
- `200 OK`: The request was successful.
- `400 Bad Request`: The request was invalid.
- `500 Internal Server Error`: An unexpected error occurred.

## Conclusion
Integrating the LLM service within the hagamesai project enhances the gaming experience by providing intelligent and responsive AI capabilities. Ensure that the necessary configurations are set up properly and that the API endpoints are utilized as intended.

For further updates, please refer to the project's [roadmap](roadmap.md) and API overview documentation.