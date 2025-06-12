"""Main application module for HAGAME AI Engine."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

from api.routers import auth, users, games, ai_engine
from core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="HAGAME AI Engine",
    description="Advanced AI system for game environments",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(games.router)
app.include_router(ai_engine.router)


@app.on_event("startup")
async def startup_event():
    """Initialize services on application startup."""
    logger.info("Starting HAGAME AI Engine")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on application shutdown."""
    logger.info("Shutting down HAGAME AI Engine")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "HAGAME AI Engine",
        "version": "0.1.0",
        "status": "running"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
