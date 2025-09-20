from fastapi import FastAPI
from app.api import auth, gmail, ai
from app.database import init_db
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(gmail.router, prefix="/api/gmail", tags=["gmail"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])

@app.on_event("startup")
def startup():
    init_db()
