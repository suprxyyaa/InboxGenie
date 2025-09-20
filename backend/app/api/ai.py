from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_services import rewrite_tone

router = APIRouter()

class ToneReq(BaseModel):
    text: str
    tone: str

@router.post("/rewrite")
def rewrite(req: ToneReq):
    return {"converted": rewrite_tone(req.text, req.tone)}
