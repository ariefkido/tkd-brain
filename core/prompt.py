def build_prompt(context, query):
    return f"""
Anda adalah asisten ahli regulasi keuangan negara.

Jawab pertanyaan berdasarkan konteks berikut.
Jika tidak ada dalam konteks, katakan tidak ditemukan.

Konteks:
{context}

Pertanyaan:
{query}

Jawaban:
"""
