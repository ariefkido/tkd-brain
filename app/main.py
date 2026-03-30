import streamlit as st
from core.rag import ask
from core.formatter import format_answer

st.title("🧠 TKD Brain")

query = st.text_input("Tanya peraturan:")

if query:
    answer, docs = ask(query)
    answer, sources = format_answer(answer, docs)

    st.write("### Jawaban")
    st.write(answer)

    st.write("### Sumber")
    for s in sources:
        st.write(f"- {s}")
