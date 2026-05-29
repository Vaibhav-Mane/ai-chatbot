from app.services.knowledge_service import (
    save_knowledge
)

knowledge = [

    "FastAPI is a Python framework",

    "Ollama runs local LLMs",

    "Embeddings convert text into vectors",

    "SQLAlchemy is an ORM"

]

for item in knowledge:

    save_knowledge(item)

print("Knowledge ingested")