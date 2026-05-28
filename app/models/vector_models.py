from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Memory(Base):

    __tablename__="memory"

    id=Column(
        Integer,
        primary_key=True
    )

    user_id=Column(
        String
    )
    
    session_id=Column(String)
    
    text=Column(
        String
    )

    embedding=Column(
        String
    )