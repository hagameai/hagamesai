from fastapi import APIRouter, HTTPException, Depends
from schemas.llm_request import LLMRequest, LLMResponse
from core.auth import get_current_user
from llm_service.service import process_llm_request

router = APIRouter()

@router.post("/llm/request", response_model=LLMResponse)
async def request_llm_service(llm_request: LLMRequest, current_user: str = Depends(get_current_user)):
    """
    Endpoint to handle LLM requests.

    Args:
        llm_request (LLMRequest): The LLM request data.
        current_user (str): The current user's identifier, retrieved through authentication.

    Returns:
        LLMResponse: The response from the LLM service.
    """
    try:
        response = await process_llm_request(llm_request, current_user)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
