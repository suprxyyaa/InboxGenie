# backend/app/utils/config.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Settings:
    """
    Application configuration settings.
    Reads values from environment variables.
    """
    PROJECT_NAME: str = "Inbox Genie"
    PROJECT_VERSION: str = "1.0.0"

    # Gmail API Credentials (load from environment)
    GMAIL_API_CLIENT_SECRET_FILE: str = os.getenv("GMAIL_API_CLIENT_SECRET_FILE")
    GMAIL_API_SCOPES: list[str] = ["https://www.googleapis.com/auth/gmail.readonly"]

    # AI Service (e.g., OpenAI or Google Gemini)
    AI_API_KEY: str = os.getenv("AI_API_KEY")
    
    # Secret key for JWT authentication
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "a_very_secret_key")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()