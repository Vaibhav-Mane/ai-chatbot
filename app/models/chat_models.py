from sqlalchemy import Column, Integer, String
from app.database import Base


class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    role = Column(String)
    content = Column(String)
    
