# backend/app/routes/ai.py
from fastapi import APIRouter, Depends
from app.models.email import EmailSummary, GeneratedReply
from app.services.ai_service import AIService
from app.services.gmail_service import GmailService
from app.utils.config import settings

# Placeholder for dependency injection
def get_user_credentials():
    return {"token": "fake-user-auth-token"}

router = APIRouter()

@router.post("/summarize", response_model=EmailSummary)
def summarize_email(email_id: str, credentials: dict = Depends(get_user_credentials)):
    """
    Summarize a specific email.
    """
    gmail_service = GmailService(credentials)
    ai_service = AIService(api_key=settings.AI_API_KEY)

    email_details = gmail_service.get_email_details(email_id)
    summary = ai_service.summarize_text(email_details.get("body", ""))
    
    return {"email_id": email_id, "summary": summary}