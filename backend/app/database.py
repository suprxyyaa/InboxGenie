from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings
from typing import Generator

_engine = create_engine(settings.DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(_engine)

def get_session() -> Generator[Session, None, None]:
    with Session(_engine) as s:
        yield s
