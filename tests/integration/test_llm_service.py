import pytest
from httpx import AsyncClient
from fastapi import FastAPI

# Import the FastAPI app
from llm_service.service import app

@pytest.mark.asyncio
async def test_llm_service_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/llm/service-endpoint")  # Replace with actual endpoint
        assert response.status_code == 200
        assert "expected_key" in response.json()  # Replace with expected response structure

@pytest.mark.asyncio
async def test_llm_service_invalid_request():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/llm/service-endpoint", json={"invalid_key": "value"})  # Replace with actual endpoint and invalid data
        assert response.status_code == 422  # Expecting validation error
