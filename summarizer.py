import re

def summarize_text(model, user_text, length="Medium"):
    if length == "Short":
        instruction = "Summarize in 2-3 sentences."
    elif length == "Medium":
        instruction = "Summarize in 4-6 sentences."
    else:
        instruction = "Summarize in detail, around 8-10 sentences."

    prompt = f"{instruction}\n\nText:\n{user_text}"
    response = model.generate_content(prompt)
    return response.text.strip()


def summarize_and_score(article, model, query):
    text = article["description"] or article["title"]
    prompt = f"""
    Summarize this {query} news article in 3 sentences.
    Then rate its relevance to the {query} industry on a scale of 1 to 10.
    Please format the relevance rating as: Relevance: X (just a number).
    
    Article:
    {text}
    """
    response = model.generate_content(prompt).text

    # Extract relevance score
    match = re.search(r"(\d+)", response)
    score = int(match.group(1)) if match else 5

    # Remove relevance line
    lines = response.split("\n")
    summary = "\n".join([l for l in lines if "Relevance" not in l])

    return summary.strip(), score
