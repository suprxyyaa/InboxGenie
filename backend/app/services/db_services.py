from sqlmodel import select
from app.database import get_session
from app.models.user import User
from app.models.email import Email
from app.core.security import hash_password, verify_password
from typing import Optional
from contextlib import contextmanager

# small wrapper functions. Use dependency injection in routers.
def create_user(session, email: str, password: str) -> User:
    u = User(email=email, hashed_password=hash_password(password))
    session.add(u); session.commit(); session.refresh(u)
    return u

def get_user_by_email(session, email: str) -> Optional[User]:
    return session.exec(select(User).where(User.email == email)).first()

def save_email(session, user_id: int, msg: dict) -> Email:
    existing = session.exec(select(Email).where(Email.gmail_id == msg["id"])).first()
    if existing:
        return existing
    e = Email(
        gmail_id=msg["id"],
        user_id=user_id,
        thread_id=msg.get("threadId"),
        subject=msg.get("subject"),
        sender=msg.get("from"),
        snippet=msg.get("snippet"),
        raw_body=msg.get("raw"),
        received_at=msg.get("internalDate")
    )
    session.add(e); session.commit(); session.refresh(e)
    return e
