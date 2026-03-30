def process_data(data):
    processed = []

    for item in data:
        new_item = item.copy()

        new_item["id"] = f"{item['source']}_{item['pasal']}_{item['ayat']}"

        new_item["embedding_text"] = f"""
        {item['full_context']}
        
        {item['text']}
        """

        processed.append(new_item)

    return processed
