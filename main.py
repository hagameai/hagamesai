from fastapi import FastAPI
from core.database import get_async_session
from api.auth import router as auth_router
from api.users import router as users_router

app = FastAPI(title="HAGAME Backend API")

app.include_router(auth_router)
app.include_router(users_router)


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
