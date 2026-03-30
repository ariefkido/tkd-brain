from ingestion.loader import load_json
from ingestion.processor import process_data
from ingestion.embedder import build_db

def main():
    data = load_json("data/raw/data.json")
    processed = process_data(data)
    build_db(processed)

    print("✅ Ingestion selesai!")

if __name__ == "__main__":
    main()
