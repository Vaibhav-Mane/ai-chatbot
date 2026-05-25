from app.database import SessionLocal
from app.models.chat_models import Chat

chat_history = []

def add_message(user_id, role, content):
    db= SessionLocal()
    message = Chat(user_id=user_id, role=role, content=content)
    db.add(message)
    db.commit()
    db.close()

def get_message(user_id,limit=10, offset=0):
    db= SessionLocal()
    messages = (db.query(Chat)
                .filter(Chat.user_id == user_id)
                .order_by(Chat.id.desc())
                .limit(limit)
                .offset(offset)
                .all())
    db.close()
    messages.reverse()
    return [{"role": m.role, "content": m.content,"time": m.created_at} for m in messages]

def clear_history():
    db= SessionLocal()
    db.query(Chat).delete()
    db.commit()
    db.close()
