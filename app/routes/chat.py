from fastapi import APIRouter, BackgroundTasks
from app.schemas.chat_schema import ChatRequest
from app.services.ai_service import ask_ai
from app.services.memory_service import clear_history, get_message
from app.services.summary_service import get_summary
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest, background_tasks: BackgroundTasks):
    generator = ask_ai(request.user_id, request.message, background_tasks)
    
    return StreamingResponse(generator, media_type="text/plain")

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

@router.get("/summary")
def summary():

    return {

        "summary":
        get_summary()

    }