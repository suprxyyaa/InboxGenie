from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from app.core.config import settings
from app.database import get_session
from sqlmodel import Session, select
from app.services.gmail_service import GmailClient
from app.services.db_services import save_email, get_user_by_email
from pydantic import BaseModel
import requests

router = APIRouter()

OAUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
SCOPES = "https://www.googleapis.com/auth/gmail.readonly openid email profile"

class GmailAuthResp(BaseModel):
    url: str

@router.get("/auth", response_model=GmailAuthResp)
def gmail_auth():
    params = {
        "client_id": settings.GMAIL_CLIENT_ID,
        "redirect_uri": settings.GMAIL_REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPES,
        "access_type": "offline",
        "prompt": "consent"
    }
    return {"url": f"{OAUTH_URL}?{urlencode(params)}"}

@router.get("/callback")
def gmail_callback(code: str, request: Request, session: Session = Depends(get_session)):
    # exchange code for token
    data = {
        "code": code,
        "client_id": settings.GMAIL_CLIENT_ID,
        "client_secret": settings.GMAIL_CLIENT_SECRET,
        "redirect_uri": settings.GMAIL_REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    r = requests.post(TOKEN_URL, data=data, timeout=15).json()
    # caller must link returned tokens to a user in your flow.
    return r

@router.post("/sync/{user_id}")
def sync_emails(user_id: int, session: Session = Depends(get_session)):
    # Expect stored token dict under DB or external store.
    # For demo we expect token in body-less placeholder: look up a token store in production.
    # Here we simulate by rejecting if not found.
    # Implementers: store token dict with refresh_token and access_token tied to user id.
    raise HTTPException(501, "token-store integration required. Use the /callback to retrieve and save tokens then call this endpoint.")
