from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "InboxGenie"
    DATABASE_URL: str = "sqlite:///./inboxgenie.db"
    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXP_SECONDS: int = 3600
    GMAIL_CLIENT_ID: str = ""
    GMAIL_CLIENT_SECRET: str = ""
    GMAIL_REDIRECT_URI: str = "http://localhost:8000/api/gmail/callback"
    OPENAI_API_KEY: str = ""
    SYNC_MAX_RESULTS: int = 50

    class Config:
        env_file = ".env"

settings = Settings()
