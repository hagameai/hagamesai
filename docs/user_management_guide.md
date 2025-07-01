# User Management Guide

This guide provides an overview of the user management features available in the hagamesai project. The user management system includes functionalities for user registration, authentication, and profile management. It is designed to ensure secure interactions and ease of use for end users.

## Features

### User Registration
- **Endpoint**: `POST /api/auth/register`
- **Description**: Allows new users to create an account.
- **Request Body**:
  - `username`: A unique identifier for the user.
  - `password`: A secure password for account access.
  - `email`: The user's email address for account verification.

- **Response**:
  - `201 Created`: User successfully registered.
  - `400 Bad Request`: Validation errors or username already taken.

### User Login
- **Endpoint**: `POST /api/auth/login`
- **Description**: Authenticates a user and provides a JWT token.
- **Request Body**:
  - `username`: The user's unique identifier.
  - `password`: The user's password.

- **Response**:
  - `200 OK`: JWT token is returned for further authenticated requests.
  - `401 Unauthorized`: Invalid credentials.

### User Profile Management
- **Endpoints**:
  - `GET /api/users/me`: Retrieves the currently authenticated user's profile.
  - `PUT /api/users/me`: Updates the user's profile information.
- **Request Body for Update**:
  - `email`: Updated email address.
  - `password`: Updated password (optional).

- **Response**:
  - `200 OK`: User profile updated successfully.
  - `404 Not Found`: User does not exist.

## Security Considerations
- Passwords must be hashed before storage.
- Implement measures to prevent brute force attacks on login endpoints.
- Consider implementing two-factor authentication for added security.

## Conclusion
This guide provides the essential information for developers and users regarding the user management features of hagamesai. For further details, please refer to the API documentation and the source code in the `api/auth.py` and `core/auth.py` files.