# backend/app/routes/email.py
from fastapi import APIRouter, Depends
from typing import List
from app.models.email import Email
from app.services.gmail_service import GmailService

# This is a placeholder for dependency injection of an authenticated user's credentials
def get_user_credentials():
    return {"token": "fake-user-auth-token"}

router = APIRouter()

@router.get("/", response_model=List[Email])
def get_emails(credentials: dict = Depends(get_user_credentials)):
    """
    Retrieve a list of emails.
    """
    gmail_service = GmailService(credentials)
    emails = gmail_service.list_emails()
    return emails