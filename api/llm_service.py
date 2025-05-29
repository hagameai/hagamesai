from fastapi import APIRouter, HTTPException
from llm_service.schemas import LLMRequest, LLMResponse
from llm_service.service import process_llm_request

router = APIRouter()

@router.post("/llm/request", response_model=LLMResponse)
async def llm_request(request: LLMRequest):
    """
    Endpoint to handle requests to the LLM service.

    - **request**: LLMRequest - The input data for the LLM service.

    Returns a LLMResponse containing the LLM's output.
    """
    try:
        response = await process_llm_request(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/llm/status")
async def llm_status():
    """
    Endpoint to check the status of the LLM service.

    Returns a simple status message.
    """
    return {"status": "LLM service is running"}
