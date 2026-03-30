from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from config.settings import CHROMA_DB_DIR, EMBEDDING_MODEL

def build_db(data):
    embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    texts = [d["embedding_text"] for d in data]

    metadatas = []
    for d in data:
        metadatas.append({
            "id": d["id"],
            "source": d["source"],
            "bab": d["bab"],
            "pasal": d["pasal"],
            "ayat": d["ayat"],
            "full_context": d["full_context"]
        })

    db = Chroma.from_texts(
        texts=texts,
        embedding=embedding,
        metadatas=metadatas,
        persist_directory=CHROMA_DB_DIR
    )

    db.persist()
