import json

from app.database import SessionLocal

from app.models.knowledge_models import Knowledge

from app.services.embedding_service import (
    create_embedding
)


def save_knowledge(text,document_name):

    db = SessionLocal()

    exists = (

        db.query(Knowledge)

        .filter(
            Knowledge.text == text
        )

        .first()

    )

    if exists:

        db.close()

        return

    embedding = create_embedding(text)

    row = Knowledge(

        text=text,
        document_name=document_name,

        embedding=json.dumps(
            embedding
        )

    )

    db.add(row)

    db.commit()

    db.close()