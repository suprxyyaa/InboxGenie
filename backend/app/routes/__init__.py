# backend/app/routes/__init__.py
from fastapi import APIRouter
from . import auth, email, ai

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(email.router, prefix="/emails", tags=["emails"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])