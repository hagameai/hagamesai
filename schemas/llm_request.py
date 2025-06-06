from pydantic import BaseModel, Field
from typing import List, Optional

class LLMPrompt(BaseModel):
    prompt: str = Field(..., description="The text prompt for the LLM to process.")
    max_tokens: Optional[int] = Field(100, description="Maximum number of tokens to generate in the response.")
    temperature: Optional[float] = Field(0.7, description="Sampling temperature. Higher value means more randomness.")
    top_p: Optional[float] = Field(1.0, description="Nucleus sampling parameter. Only considers the top_p probability mass.")

class LLMRequest(BaseModel):
    model: str = Field(..., description="The identifier of the model to use for the request.")
    prompt: LLMPrompt = Field(..., description="The prompt details for the LLM.")
    user_id: Optional[str] = Field(None, description="ID of the user making the request.")
    session_id: Optional[str] = Field(None, description="ID of the session for tracking requests.")

class LLMResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the request was successful.")
    data: List[str] = Field(..., description="List of generated responses from the LLM.")
    error: Optional[str] = Field(None, description="Error message if the request failed.")