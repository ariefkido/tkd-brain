import os
import json
from ingestion.loader import load_json
from ingestion.processor import process_data
from ingestion.embedder import build_db

DATA_DIR = "data/raw"

def main():
    all_data = []

    json_files = [
        f for f in os.listdir(DATA_DIR)
        if f.endswith(".json") and f != "readme.md"
    ]

    if not json_files:
        print("❌ Tidak ada file JSON di folder data/raw")
        return

    print(f"📂 Ditemukan {len(json_files)} file JSON, mulai memuat...")

    for filename in sorted(json_files):
        path = os.path.join(DATA_DIR, filename)
        try:
            data = load_json(path)
            if isinstance(data, list):
                all_data.extend(data)
            else:
                all_data.append(data)
            print(f"  ✅ {filename} ({len(data)} entri)")
        except Exception as e:
            print(f"  ⚠️  Gagal memuat {filename}: {e}")

    print(f"\n📊 Total {len(all_data)} entri dimuat, mulai proses embedding...")

    processed = process_data(all_data)
    build_db(processed)

    print("✅ Ingestion selesai!")

if __name__ == "__main__":
    main()
