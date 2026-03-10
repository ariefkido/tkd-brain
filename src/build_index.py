from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os

DATA_DIR = "data"
INDEX_DIR = "index"
EMBED_MODEL = "intfloat/multilingual-e5-base"

def main():
    # Validasi folder data
    if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
        print(f"Error: Folder '{DATA_DIR}' tidak ada atau kosong.")
        return

    print(f"Memuat embedding model '{EMBED_MODEL}'...")
    print("(Proses ini mungkin memakan waktu jika model belum ter-download)")
    
    try:
        Settings.embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)
    except Exception as e:
        print(f"Gagal memuat model: {e}")
        return

    print("Memuat dokumen dari folder data...")
    try:
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
    except Exception as e:
        print(f"Gagal memuat dokumen: {e}")
        return

    if not documents:
        print("Tidak ada dokumen yang berhasil dimuat.")
        return

    print(f"{len(documents)} dokumen berhasil dimuat.")

    os.makedirs(INDEX_DIR, exist_ok=True)

    print("Membuat vector index...")
    try:
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
    except Exception as e:
        print(f"Gagal membuat index: {e}")
        return

    print("Menyimpan index...")
    try:
        index.storage_context.persist(persist_dir=INDEX_DIR)
        print(f"Index berhasil disimpan di folder '{INDEX_DIR}'")
    except Exception as e:
        print(f"Gagal menyimpan index: {e}")

if __name__ == "__main__":
    main()
