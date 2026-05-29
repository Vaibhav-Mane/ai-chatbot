from app.services.knowledge_service import (
    save_knowledge
)
from app.utils.chunking import chunk_text

documents = {

    "fastapi_doc": """

    FastAPI is a modern Python framework.

    FastAPI supports async APIs.

    """,

    "ai_doc": """

    Embeddings convert text into vectors.

    RAG means Retrieval Augmented Generation.

    """

}


for doc_name, content in documents.items():

    chunks = chunk_text(
        content,
        chunk_size=5
    )

    for chunk in chunks:

        save_knowledge(
            doc_name,
            chunk
        )

print("Chunk ingestion completed")