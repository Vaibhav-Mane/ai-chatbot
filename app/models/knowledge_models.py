from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.database import Base


class Knowledge(Base):

    __tablename__ = "knowledge"

    id = Column(
        Integer,
        primary_key=True
    )

    text = Column(String)

    embedding = Column(String)