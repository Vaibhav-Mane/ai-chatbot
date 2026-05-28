from app.database import SessionLocal
from app.models.chat_models import Chat
import json

from app.models.vector_models import Memory
from app.services.embedding_service import (
    create_embedding,
    cosine_similarity
)

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


def save_memory(
    user_id,
    text
):

    db=SessionLocal()

    embedding=create_embedding(
        text
    )

    memory=Memory(

        user_id=user_id,

        text=text,

        embedding=json.dumps(
            embedding
        )

    )

    db.add(memory)

    db.commit()

    db.close()

def find_similar_memory(
    user_id,
    question
):

    db=SessionLocal()

    query_embedding=(
        create_embedding(
            question
        )
    )

    rows=(

        db.query(Memory)

        .filter(
            Memory.user_id==user_id
        )

        .all()

    )

    best=[]

    for row in rows:

        emb=json.loads(
            row.embedding
        )

        score=cosine_similarity(
            query_embedding,
            emb
        )

        if score>.40:

            best.append(
                row.text
            )

    db.close()

    return best