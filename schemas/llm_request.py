from pydantic import BaseModel, Field
from typing import Optional

class LLMRequest(BaseModel):
    prompt: str = Field(..., description="The input prompt for the LLM.")
    model: str = Field(..., description="The name of the LLM model to use.")
    max_tokens: Optional[int] = Field(100, ge=1, description="The maximum number of tokens to generate.")
    temperature: Optional[float] = Field(0.7, ge=0.0, le=1.0, description="Sampling temperature for the model.")
    top_p: Optional[float] = Field(1.0, ge=0.0, le=1.0, description="Cumulative probability for top-p sampling.")
    stop: Optional[list] = Field(None, description="List of stop sequences for the LLM.")

    class Config:
        schema_extra = {
            "example": {
                "prompt": "What is the capital of France?",
                "model": "gpt-3.5-turbo",
                "max_tokens": 50,
                "temperature": 0.5,
                "top_p": 1.0,
                "stop": ["\n"]
            }
        }
