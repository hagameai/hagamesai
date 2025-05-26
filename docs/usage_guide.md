# Usage Guide for API Endpoints

This guide provides examples of how to use the API endpoints in the `hagamesai` backend service. Each section outlines the request format, required parameters, and example responses for common API functionalities.

## User Authentication

### Register a New User
**Endpoint:** `POST /api/auth/register`

**Request Body:**
```json
{
    "username": "example_user",
    "password": "securepassword",
    "email": "user@example.com"
}
```

**Response:**
- **201 Created** on success:
```json
{
    "message": "User registered successfully."
}
```
- **400 Bad Request** on validation error:
```json
{
    "detail": "Username already exists."
}
```

### User Login
**Endpoint:** `POST /api/auth/login`

**Request Body:**
```json
{
    "username": "example_user",
    "password": "securepassword"
}
```

**Response:**
- **200 OK** on success:
```json
{
    "access_token": "your_jwt_token",
    "token_type": "bearer"
}
```
- **401 Unauthorized** if credentials are invalid:
```json
{
    "detail": "Invalid username or password."
}
```

## Game Management

### Create a New Game
**Endpoint:** `POST /api/games`

**Request Body:**
```json
{
    "game_name": "Chess",
    "description": "A strategic board game for two players."
}
```

**Response:**
- **201 Created** on success:
```json
{
    "game_id": "123",
    "message": "Game created successfully."
}
```

### Get Game Details
**Endpoint:** `GET /api/games/{game_id}`

**Response:**
- **200 OK** on success:
```json
{
    "game_id": "123",
    "game_name": "Chess",
    "description": "A strategic board game for two players."
}
```
- **404 Not Found** if the game does not exist:
```json
{
    "detail": "Game not found."
}
```

## AI Engine Services

### Request AI Service
**Endpoint:** `POST /api/llm/request`

**Request Body:**
```json
{
    "input_text": "What is the capital of France?"
}
```

**Response:**
- **200 OK** on success:
```json
{
    "response": "The capital of France is Paris."
}
```
- **500 Internal Server Error** if the AI service fails:
```json
{
    "detail": "Error processing request."
}
```

## Conclusion

This usage guide serves as a reference for interacting with the API endpoints of `hagamesai`. Always ensure to handle responses properly, especially error cases, to provide a smooth user experience.