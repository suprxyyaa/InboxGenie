# backend/app/__init__.py
from fastapi import FastAPI
from app.utils.config import settings
from app.routes import api_router

def create_app() -> FastAPI:
    """
    Application factory for creating the FastAPI app instance.
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )

    # Include the main API router
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/")
    def read_root():
        return {"message": f"Welcome to {settings.PROJECT_NAME}"}

    return app