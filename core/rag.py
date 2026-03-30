import google.generativeai as genai
from google.api_core import retry
from core.retriever import retrieve
from core.prompt import build_prompt
from config.settings import GOOGLE_API_KEY, LLM_MODEL

genai.configure(api_key=GOOGLE_API_KEY)

def ask(query):
    docs = retrieve(query)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = build_prompt(context, query)

    model = genai.GenerativeModel(LLM_MODEL)
    response = model.generate_content(
        prompt,
        request_options={"timeout": 60},  # timeout eksplisit 60 detik
    )

    return response.text, docs
