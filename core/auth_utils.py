import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class AuthUtils:
    """
    Utility functions for authentication processes.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using SHA-256.
        
        :param password: The plaintext password to be hashed.
        :return: The hashed password as a hexadecimal string.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def generate_jwt_token(user_id: str, secret: str, expiration_minutes: int = 60) -> str:
        """
        Generate a JSON Web Token (JWT) for a user.
        
        :param user_id: The ID of the user.
        :param secret: The secret key used to encode the token.
        :param expiration_minutes: The expiration time of the token in minutes.
        :return: The encoded JWT as a string.
        """
        expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        # Normally you would use a library like PyJWT to create the token.
        # Here we would just return a dummy string for demonstration purposes.
        return f"token-{user_id}-{expiration.timestamp()}"

    @staticmethod
    def validate_jwt_token(token: str, secret: str) -> Optional[Dict[str, Any]]:
        """
        Validate the JWT token and return the payload.
        
        :param token: The JWT token to validate.
        :param secret: The secret key used to decode the token.
        :return: The payload if valid, otherwise None.
        """
        # Normally you would use a library like PyJWT to decode and validate the token.
        # Here we would just return a dummy payload for demonstration purposes.
        if "token-" in token:
            parts = token.split("-")
            return {"user_id": parts[1], "exp": float(parts[2])}
        return None
