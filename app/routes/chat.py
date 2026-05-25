from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.ai_service import ask_ai
from app.services.memory_service import clear_history, get_message

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    response = ask_ai(request.message)
    
    return{"reply": response}

@router.get("/history")
def get_history():
    getmessage= get_message()
    return {"messages": getmessage}

@router.post("/reset")
def reset():
    clear_history()
    return {
        "success": True,
        "message": "chat history cleared"
    }