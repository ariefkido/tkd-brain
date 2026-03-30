import streamlit as st
from core.rag import ask
from core.formatter import format_answer

st.set_page_config(page_title="TKD Brain", layout="wide")

st.title("🧠 TKD Brain")
st.write("Tanya jawab peraturan berbasis dokumen")

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
