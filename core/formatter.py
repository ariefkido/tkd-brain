def format_answer(answer, docs):
    sources = []

    for d in docs:
        meta = d.metadata
        sources.append(
            f"{meta['source']} - {meta['full_context']}"
        )

    sources = list(set(sources))

    return answer, sources
