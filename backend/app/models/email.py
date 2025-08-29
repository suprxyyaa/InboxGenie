# backend/app/models/email.py
from pydantic import BaseModel
from typing import Optional

class Email(BaseModel):
    id: str
    subject: str
    sender: str
    snippet: str
    body: Optional[str] = None # The full body will be loaded on demand

class EmailSummary(BaseModel):
    email_id: str
    summary: str

class GeneratedReply(BaseModel):
    email_id: str
    reply_text: str