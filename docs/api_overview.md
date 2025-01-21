# API Overview

This document provides a detailed overview of the API endpoints available in the `hagamesai` project. The API is built using FastAPI and offers various functionalities to support human-vs-AI game scenarios, advanced cognitive modeling, and LLM-powered services.

## Base URL
The base URL for all the API endpoints is:
```
http://<your-domain>/api
```

## Authentication
Most endpoints require user authentication. You can obtain a JWT token by using the `/auth/login` endpoint after registering a user via `/auth/register`.

## Endpoints

### User Endpoints

1. **Register User**  
   - **Endpoint:** `/auth/register`  
   - **Method:** `POST`  
   - **Request Body:**
     ```json
     {
       "username": "<string>",
       "password": "<string>"
     }
     ```
   - **Response:**  
     - **201 Created** on successful registration.
     - **400 Bad Request** if the input data is invalid.

2. **Login User**  
   - **Endpoint:** `/auth/login`  
   - **Method:** `POST`  
   - **Request Body:**
     ```json
     {
       "username": "<string>",
       "password": "<string>"
     }
     ```
   - **Response:**  
     - **200 OK** with JWT token on successful login.
     - **401 Unauthorized** if credentials are invalid.

### Game Management Endpoints

1. **Get Game Definitions**  
   - **Endpoint:** `/games/definitions`  
   - **Method:** `GET`  
   - **Response:**  
     - **200 OK** with a list of game definitions.

2. **Create Game Instance**  
   - **Endpoint:** `/games/instances`  
   - **Method:** `POST`  
   - **Request Body:**
     ```json
     {
       "game_id": "<string>",
       "user_id": "<string>"
     }
     ```
   - **Response:**  
     - **201 Created** on successful creation.
     - **400 Bad Request** if the input data is invalid.

### AI Services Endpoints

1. **AI Engine Prediction**  
   - **Endpoint:** `/llm/predict`  
   - **Method:** `POST`  
   - **Request Body:**
     ```json
     {
       "input_data": "<string>"
     }
     ```
   - **Response:**  
     - **200 OK** with AI prediction result.

## Error Handling
All API responses include a status code and a message. Common status codes include:
- **200 OK:** Successful request.
- **201 Created:** Resource successfully created.
- **400 Bad Request:** Invalid input data.
- **401 Unauthorized:** Authentication error.
- **404 Not Found:** Resource not found.
- **500 Internal Server Error:** An unexpected error occurred.

## Conclusion
This overview provides a high-level understanding of the available API endpoints in the `hagamesai` project. For more detailed information about specific endpoints, refer to the endpoint documentation in the respective modules.