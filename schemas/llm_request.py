from pydantic import BaseModel, Field
from typing import List, Optional

class LLMRequest(BaseModel):
    prompt: str = Field(..., description="The input prompt for the language model.")
    max_tokens: int = Field(150, ge=1, le=2048, description="Maximum number of tokens to generate.")
    temperature: float = Field(1.0, ge=0.0, le=2.0, description="Controls randomness in the output.")
    top_p: float = Field(1.0, ge=0.0, le=1.0, description="Nucleus sampling parameter.")
    frequency_penalty: float = Field(0.0, ge=-2.0, le=2.0, description="Penalty for using frequent tokens.")
    presence_penalty: float = Field(0.0, ge=-2.0, le=2.0, description="Penalty for using new tokens.")
    stop: Optional[List[str]] = Field(None, description="List of tokens to stop generation.")

    class Config:
        schema_extra = {
            "example": {
                "prompt": "Once upon a time, in a land far away...",
                "max_tokens": 100,
                "temperature": 0.7,
                "top_p": 0.9,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "stop": ["\n", "END"]
            }
        }