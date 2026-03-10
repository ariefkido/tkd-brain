from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

INDEX_DIR = "index"

def main():

    print("Loading embedding model...")

    Settings.embed_model = HuggingFaceEmbedding(
        model_name="intfloat/multilingual-e5-base"
    )

    print("Memuat index...")

    storage_context = StorageContext.from_defaults(
        persist_dir=INDEX_DIR
    )

    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine(
        similarity_top_k=5
    )

    print("\nAI TKD siap digunakan.")
    print("Ketik 'exit' untuk keluar.\n")

    while True:

        question = input("Tanya: ")

        if question.lower() == "exit":
            break

        response = query_engine.query(question)

        print("\nJawaban:\n")
        print(response)
        print("\n-------------------\n")

if __name__ == "__main__":
    main()