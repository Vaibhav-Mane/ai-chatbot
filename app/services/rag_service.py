from app.services.embedding_service import (
    create_embedding,
    cosine_similarity
)
from app.database import SessionLocal
from app.models.knowledge_models import Knowledge
import json

def retrieve_knowledge(question):
    db = SessionLocal()
    
    question_embedding = (
        create_embedding(question)
    )
    rows = db.query(Knowledge).all()
    
    best_match = []

    for row in rows:
        emb = json.loads(
            row.embedding
        )

        print(
        f"{row.document_name}"
        f" -> {row.text}"
        f" -> {score}"
            )
        
        score = cosine_similarity(

            question_embedding,

            emb

        )

        print(
            f"{row.text} -> {score}"
        )

        if score > 0.5:

            best_match.append(
                row.text
            )
    db.close()
    return best_match