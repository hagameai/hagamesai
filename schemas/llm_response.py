from pydantic import BaseModel, Field
from typing import Any, List, Optional

class LLMResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the response was successful")
    message: Optional[str] = Field(None, description="Optional message providing additional context")
    data: List[Any] = Field(..., description="List of data items returned by the LLM")

class LLMError(BaseModel):
    success: bool = Field(False, description="Indicates that there was an error")
    error_code: str = Field(..., description="Code representing the error type")
    error_message: str = Field(..., description="Description of the error")
