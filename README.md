# 📰✨ [AI Summarizer App](https://mainpy-jvpwhe72bxjmnlhnrjhgyh.streamlit.app/)

A simple **AI-powered text and news summarizer** built with **Streamlit** and **Google Gemini API**.
---

## 🚀 Features
- **Text Summarizer:** Paste any text and get concise AI-generated summaries in short, medium, or long formats.  
- **News Summarizer:** Fetch live news using the NewsAPI and summarize the articles in a selected category.  
- **AI Scoring:** Ranks news articles by relevance using Gemini’s evaluation.  
- **Streamlit UI:** Clean, interactive web interface.  

---

## 🧩 Project Structure
AI-Summarizer/
│

├── main.py # Main Streamlit app

├── summarizer.py # Summarization logic using Gemini

├── news_fetcher.py # Fetches live news from NewsAPI

├── config.py # Stores API keys

├── requirements.txt # Python dependencies (optional)

└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### Clone the repository
```bash
git clone https://github.com/your-username/ai-summarizer.git
cd ai-summarizer
```
You'll also need a **Google Gemini API key**, which you can get for free at

👉 **[Google AI Studio](https://aistudio.google.com/api-keys)**

## 🧠 Usage

### Run the app:
```bash
streamlit run main.py
```
### OR
**[Streamlit Deployment](https://mainpy-jvpwhe72bxjmnlhnrjhgyh.streamlit.app/)**

---

## 🔹 Text Summarizer Mode
- Select "Text Summarizer" from the sidebar.
- Paste your text.
- Choose a summary length (Short / Medium / Long).
- Click Summarize Text — your summary appears instantly!

## 🔹 News Summarizer Mode
- Choose "News Summarizer" from the sidebar.
- Select a category (e.g., Technology, Sports, Business).
- Enter the number of articles to fetch.
- Click Fetch & Summarize News to view top summarized articles ranked by relevance.
