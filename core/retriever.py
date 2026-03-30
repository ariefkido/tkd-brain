from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from config.settings import CHROMA_DB_DIR, EMBEDDING_MODEL, TOP_K

MAX_CHARS_PER_DOC = 2000  # ~500 token per dokumen

embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embedding
)

def retrieve(query, k=TOP_K, filters=None):
    docs = db.similarity_search(query, k=k, filter=filters)

    # Truncate dokumen yang terlalu panjang
    for doc in docs:
        if len(doc.page_content) > MAX_CHARS_PER_DOC:
            doc.page_content = doc.page_content[:MAX_CHARS_PER_DOC] + "..."

    return docs
