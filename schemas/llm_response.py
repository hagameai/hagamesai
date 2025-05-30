from pydantic import BaseModel, Field
from typing import Any, List, Optional

class LLMResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the request was successful")
    message: Optional[str] = Field(None, description="Optional message providing additional context")
    data: List[Any] = Field(..., description="List of responses from the LLM")

    class Config:
        schema_extra = {
            "example": {
                "success": true,
                "message": "Request processed successfully",
                "data": [
                    {
                        "text": "Hello, how can I assist you today?",
                        "confidence": 0.95
                    }
                ]
            }
        }
