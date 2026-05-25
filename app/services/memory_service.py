from app.database import SessionLocal
from app.models.chat_models import Chat

chat_history = []

def add_message(role, content):
    db= SessionLocal()
    message = Chat(role=role, content=content)
    db.add(message)
    db.commit()
    db.close()

def get_message():
    db= SessionLocal()
    messages = db.query(Chat).all()
    db.close()
    return [{"role": message.role, "content": message.content} for message in messages]

def clear_history():
    db= SessionLocal()
    db.query(Chat).delete()
    db.commit()
    db.close()
