import requests

def fetch_news(query, api_key, page_size=5):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    articles = []
    if "articles" in data:
        for art in data["articles"]:
            articles.append({
                "title": art["title"],
                "url": art["url"],
                "publishedAt": art["publishedAt"],
                "description": art["description"],
                "image": art["urlToImage"]
            })
    return articles
