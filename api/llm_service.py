from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class LLMRequest(BaseModel):
    prompt: str
    max_length: int = 50

class LLMResponse(BaseModel):
    generated_text: str

@router.post("/llm/generate", response_model=LLMResponse)
async def generate_text(request: LLMRequest):
    """
    Generate text using the LLM based on the provided prompt.

    Parameters:
    - request: LLMRequest containing the prompt and max_length.

    Returns:
    - LLMResponse containing the generated text.
    """
    try:
        # Here you would normally call your LLM model to generate text
        # For example:
        generated_text = "This is a dummy response based on the prompt: " + request.prompt
        return LLMResponse(generated_text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/llm/health")
async def health_check():
    """
    Health check endpoint to ensure the LLM service is running.

    Returns:
    - A simple status message.
    """
    return {"status": "LLM service is running"}

