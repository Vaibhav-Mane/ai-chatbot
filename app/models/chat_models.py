from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Chat(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    session_id = Column(String)
    role = Column(String)
    content = Column(String)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
