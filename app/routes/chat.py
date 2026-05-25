from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.ai_service import ask_ai
from app.services.memory_service import clear_history, get_message

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    response = ask_ai(request.user_id, request.message)
    
    return{"reply": response}

@router.get("/history")
def get_history(user_id: str, limit: int = 10, offset: int = 0):
    getmessage= get_message(user_id, limit=limit, offset=offset)
    return {"messages": getmessage}

@router.post("/reset")
def reset():
    clear_history()
    return {
        "success": True,
        "message": "chat history cleared"
    }