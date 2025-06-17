# LLM Integration Guide

This document provides guidance on integrating LLM (Large Language Model) services into the hagamesai backend. This integration is crucial for enhancing the AI capabilities in human-vs-AI gameplay and cognitive modeling.

## Prerequisites

Before integrating LLM services, ensure you have the following:
- Python 3.10+
- FastAPI
- Required libraries for LLM integration (e.g., `transformers`, `torch`, etc.)

## Setting Up the LLM Service

1. **Install Required Packages**:
   
   You need to install the necessary libraries via pip:
   ```bash
   pip install transformers torch
   ```

2. **Configure the LLM Service**:
   
   In the `llm_service/service.py` file, set up the LLM model and tokenizer:
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer

   class LLMService:
       def __init__(self, model_name: str):
           self.tokenizer = AutoTokenizer.from_pretrained(model_name)
           self.model = AutoModelForCausalLM.from_pretrained(model_name)

       def generate_text(self, prompt: str, max_length: int = 50):
           inputs = self.tokenizer(prompt, return_tensors="pt")
           outputs = self.model.generate(**inputs, max_length=max_length)
           return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
   ```

3. **Integrate with FastAPI**:
   
   Create an API endpoint to utilize the LLM service in `api/llm.py`:
   ```python
   from fastapi import APIRouter, HTTPException
   from llm_service.service import LLMService

   llm_router = APIRouter()
   llm_service = LLMService("gpt2")  # Example model

   @llm_router.post("/generate")
   async def generate_text(prompt: str):
       try:
           return llm_service.generate_text(prompt)
       except Exception as e:
           raise HTTPException(status_code=500, detail=str(e))
   ```

4. **Testing the Integration**:
   
   Ensure to create unit and integration tests for the new LLM functionalities. Tests should cover:
   - Valid input generation
   - Error handling for invalid inputs

## Conclusion

This guide outlines the steps necessary for integrating LLM services into the hagamesai project. Ensure to refer to the official documentation of the libraries used for any advanced configurations and optimizations.

For further assistance, consult the project's documentation or reach out to the development team.