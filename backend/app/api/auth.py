from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_session
from app.services.db_services import create_user, get_user_by_email
from app.core.security import verify_password, create_jwt
from pydantic import BaseModel

router = APIRouter()

class RegisterReq(BaseModel):
    email: str
    password: str

class TokenResp(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/register")
def register(req: RegisterReq, session: Session = Depends(get_session)):
    if get_user_by_email(session, req.email):
        raise HTTPException(400, "email exists")
    user = create_user(session, req.email, req.password)
    return {"id": user.id, "email": user.email}

@router.post("/token", response_model=TokenResp)
def token(form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = get_user_by_email(session, form.username)
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(401, "invalid credentials")
    token = create_jwt(str(user.id))
    return {"access_token": token}
