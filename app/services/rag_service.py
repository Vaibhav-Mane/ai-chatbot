from app.services.embedding_service import (
    create_embedding,
    cosine_similarity
)


def load_knowledge():

    with open(
        "app/data/knowledge.txt",
        "r"
    ) as f:

        data = f.readlines()

    return [
        line.strip()
        for line in data
        if line.strip()
    ]


knowledge_base = []

for text in load_knowledge():

    knowledge_base.append(

        {

            "text": text,

            "embedding":
            create_embedding(text)

        }

    )


def retrieve_knowledge(question):

    question_embedding = (
        create_embedding(question)
    )

    best_match = []

    for item in knowledge_base:

        score = cosine_similarity(

            question_embedding,

            item["embedding"]

        )

        print(
            f"{item['text']} -> {score}"
        )

        if score > 0.5:

            best_match.append(
                item["text"]
            )

    return best_match