import os
from dotenv import load_dotenv

load_dotenv()

# === Google Gemini ===
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-1.5-flash")

# === ChromaDB ===
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "data/chroma_db")

# === Embedding ===
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-base")

# === Retrieval ===
TOP_K = int(os.getenv("TOP_K", "5"))
