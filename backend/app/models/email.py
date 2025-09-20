from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Email(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    gmail_id: str = Field(index=True)
    user_id: int = Field(index=True)
    thread_id: Optional[str] = None
    subject: Optional[str] = None
    sender: Optional[str] = None
    snippet: Optional[str] = None
    raw_body: Optional[str] = None
    is_spam: bool = False
    received_at: Optional[datetime] = None
