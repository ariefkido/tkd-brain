import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from config.settings import CHROMA_DB_DIR

st.set_page_config(page_title="TKD Brain", layout="wide")
st.title("🧠 TKD Brain")
st.write("Tanya jawab peraturan berbasis dokumen")

# Auto-ingest jika ChromaDB belum ada
if not os.path.exists(CHROMA_DB_DIR) or not os.listdir(CHROMA_DB_DIR):
    with st.spinner("⏳ Membangun database pertama kali, mohon tunggu..."):
        from ingestion.run_ingest import main as run_ingest
        run_ingest()
    st.success("✅ Database berhasil dibangun!")
    st.rerun()

from core.rag import ask
from core.formatter import format_answer

query = st.text_input("Masukkan pertanyaan:")

if query:
    with st.spinner("Mencari jawaban..."):
        answer, docs = ask(query)
        answer, sources = format_answer(answer, docs)

    st.subheader("Jawaban")
    st.write(answer)

    st.subheader("Sumber")
    for s in sources:
        st.write(f"- {s}")
