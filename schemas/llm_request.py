from pydantic import BaseModel, Field
from typing import Any, List, Optional

class LLMRequest(BaseModel):
    prompt: str = Field(..., description="The input prompt for the LLM")
    max_tokens: Optional[int] = Field(150, description="Maximum number of tokens to generate")
    temperature: Optional[float] = Field(0.7, description="Sampling temperature for creativity")
    top_p: Optional[float] = Field(1.0, description="Nucleus sampling parameter")
    stop: Optional[List[str]] = Field(None, description="List of stop sequences to end the generation")
    additional_params: Optional[dict[str, Any]] = Field(None, description="Any additional parameters for the LLM request")

    class Config:
        schema_extra = {
            "example": {
                "prompt": "Once upon a time...",
                "max_tokens": 100,
                "temperature": 0.8,
                "top_p": 0.9,
                "stop": ["\n"],
                "additional_params": {"key": "value"}
            }
        }
