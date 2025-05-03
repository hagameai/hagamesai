from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from core.database import get_async_session
from api.auth import router as auth_router
from api.users import router as users_router
from api.games import router as games_router
from api.ai import router as ai_router
from api.llm import router as llm_router
from core.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(title="HAGAME Backend API")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(games_router)
app.include_router(ai_router)
app.include_router(llm_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(
        f"HTTPException: {exc.detail} (status: {exc.status_code}) - Path: {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status_code": exc.status_code},
    )


@app.get("/", tags=["health"])
async def health_check():
    """Health check endpoint for service status."""
    return {"status": "ok"}

# Routers will be included here as modules are implemented

# Example root endpoint


def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
