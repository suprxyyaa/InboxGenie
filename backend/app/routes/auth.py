# backend/app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate, Token

router = APIRouter()

@router.post("/register", status_code=201)
def register_user(user: UserCreate):
    # In a real app, you would hash the password and save the user to a database.
    return {"message": f"User {user.email} registered successfully."}

@router.post("/login", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # In a real app, you would verify the user's password and create a JWT token.
    if form_data.username == "user@example.com" and form_data.password == "password":
        # This is a mock token
        return {"access_token": "fake-jwt-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")