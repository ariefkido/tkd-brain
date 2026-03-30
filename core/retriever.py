from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from config.settings import CHROMA_DB_DIR, EMBEDDING_MODEL, TOP_K

embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embedding
)

def retrieve(query, k=TOP_K, filters=None):
    return db.similarity_search(query, k=k, filter=filters)
