from pydantic import BaseModel, Field
from typing import Any, List, Optional

class LLMResponse(BaseModel):
    id: str = Field(..., description="The unique identifier for the response")
    prompt: str = Field(..., description="The input prompt given to the LLM")
    response: str = Field(..., description="The generated response from the LLM")
    tokens_used: int = Field(..., description="The number of tokens used in the response")
    completion_time: float = Field(..., description="Time taken to generate the response in seconds")
    metadata: Optional[dict[str, Any]] = Field(None, description="Optional metadata related to the response")

class LLMResponseList(BaseModel):
    responses: List[LLMResponse] = Field(..., description="List of LLM responses")
