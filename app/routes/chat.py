from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.ai_service import ask_ai

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    response = ask_ai(request.message)
    
    return{"reply": response}