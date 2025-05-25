# API Reference for hagamesai

This document serves as a detailed API reference for the endpoints available in the hagamesai project. Each endpoint is described with its functionality, required parameters, and response structure.

## Authentication

### POST /auth/login
- **Description:** Authenticate a user and return a JWT token.
- **Request Body:**
  - `email` (string): The user's email address.
  - `password` (string): The user's password.
- **Response:**
  - **200 OK**  
    - `access_token` (string): JWT token for authorized access.
    - `token_type` (string): Type of token (usually "bearer").
  - **401 Unauthorized**  
    - Error message indicating invalid credentials.


### POST /auth/register
- **Description:** Register a new user.
- **Request Body:**
  - `email` (string): The new user's email address.
  - `password` (string): The new user's password.
  - `name` (string): The user's name.
- **Response:**
  - **201 Created**  
    - `user_id` (integer): ID of the newly created user.
  - **400 Bad Request**  
    - Error message indicating validation issues.


## Game Management

### GET /games
- **Description:** Retrieve a list of all games.
- **Response:**
  - **200 OK**  
    - `games` (array): Array of game objects containing details such as ID, name, and description.


### POST /games
- **Description:** Create a new game definition.
- **Request Body:**
  - `name` (string): Name of the game.
  - `description` (string): Description of the game.
- **Response:**
  - **201 Created**  
    - `game_id` (integer): ID of the newly created game.
  - **400 Bad Request**  
    - Error message indicating validation issues.


## AI Services

### POST /llm/predict
- **Description:** Get predictions from the LLM based on input data.
- **Request Body:**
  - `input` (string): The input data for the prediction.
- **Response:**
  - **200 OK**  
    - `prediction` (string): Predicted output from the LLM.
  - **400 Bad Request**  
    - Error message indicating invalid input.


## Error Handling

All endpoints will return appropriate HTTP status codes and error messages for any failures. Common error responses include:
- **400 Bad Request:** The request was invalid.
- **401 Unauthorized:** Authentication is required or failed.
- **404 Not Found:** The requested resource was not found.
- **500 Internal Server Error:** An unexpected error occurred on the server side.

## Conclusion

This API reference provides a comprehensive overview of the endpoints available for the hagamesai project. For further assistance, please consult the project's documentation or contact the development team.