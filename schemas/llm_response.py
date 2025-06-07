from pydantic import BaseModel
from typing import Any, List, Optional

class LLMResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[List[Any]] = None

    class Config:
        schema_extra = {
            "example": {
                "success": true,
                "message": "Response retrieved successfully.",
                "data": [
                    {"id": 1, "content": "This is a sample response."},
                    {"id": 2, "content": "This is another sample response."}
                ]
            }
        }

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error_code: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "success": false,
                "message": "An error occurred.",
                "error_code": 400
            }
        }