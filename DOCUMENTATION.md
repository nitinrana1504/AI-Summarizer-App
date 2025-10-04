## 🧑‍💻 Author
**Nitin Rana**

AI & Software Enthusiast | Open to internships and collaborative projects 🤝
# 🧠 Project Documentation — AI Summarizer App

This file documents my complete journey while building the **AI Summarizer App** as part of an internship assignment.

---

## 🏁 Part 1: Setup

### ✅ Step 1: Environment Setup
- Installed **Python 3.11**
- Installed required libraries:
  ```bash
  pip install streamlit google-generativeai requests
  ```
  - Created a project folder: AI-Summarizer
  - Created GitHub repository and initial commit with .gitignore and README.md

### ✅ Step 2: API Keys
- Created a free account on [NewsAPI.org](https://newsapi.org/) to fetch real news data.
- Generated a Google Gemini API key from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/api-keys)
- Stored them securely in config.py (using placeholder for public repo):
  ```python
  NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"
  ```
---
  ## 💡 Part 2: Building the App

  ### 🧱 Step 3: News Fetcher (news_fetcher.py)
- Used requests library to call the NewsAPI endpoint.
- Extracted useful fields (title, url, description, image, published date).
- Added fetch_news() function to return structured article data.

### 🧠 Step 4: Summarizer (summarizer.py)
- Used Gemini model via google.generativeai.
- Wrote summarize_text() for general text summarization (2–10 sentences).
- Added summarize_and_score() to:
  - Summarize news in 3 sentences.
  - Rate relevance (1–10) using regex extraction.
  - Return both summary and score.

### 🧩 Step 5: Streamlit App (main.py)
- Built interactive UI with:
  - Sidebar mode switch (Text Summarizer / News Summarizer)
  - API key input field
  - Dynamic content display using Streamlit components
- Integrated all functions:
  - Configured Gemini model once API key is provided.
  - Displayed warnings, summaries, and top-ranked articles.
---
## Part 3: Testing
### ✅ Text Summarizer Tests
- Tried summarizing random Wikipedia articles.
- Verified summary length control (Short/Medium/Long).
- Ensured the app handles empty input gracefully.

### ✅ News Summarizer Tests
- Tested categories: Technology, Sports, Business.
- Displayed news summaries with images and timestamps.
- Confirmed the app shows a warning when no news is fetched.

## 🌱 Stretch Goal (Optional UI)
- Added Streamlit interface instead of plain CLI.
- The app can be deployed on Render or Streamlit Cloud with one click.

---

## 🔎 Resources Used

- [Streamlit Docs](https://docs.streamlit.io/)
- [NewsAPI Documentation](https://newsapi.org/docs)
- [Google Gemini API Reference](https://ai.google.dev/)

---

## 🎯 Reflections & Takeaways
- Learned to integrate **multiple APIs** in one project.
- Understood how to manage **API keys securely**.
- Gained experience with **Streamlit UI** and prompt design for LLMs.
- Improved problem-solving skills through documentation and iteration.

---

## 🔮 Future Improvements
- Add user authentication and persistent API key storage.
- Allow exporting summaries as PDF or text files.
- Add automatic topic detection for random news feeds.
- Deploy on Hugging Face Spaces for public demo.

---

## ✅ Final Thoughts
This project shows how a simple idea can combine **real-time data (NewsAPI)** and **AI summarization (Gemini)** in a neat, functional app.
