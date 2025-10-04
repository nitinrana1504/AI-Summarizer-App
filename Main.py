import streamlit as st
import google.generativeai as genai
from news_fetcher import fetch_news
from summarizer import summarize_text, summarize_and_score
from config import NEWS_API_KEY

# --- Streamlit UI ---
st.title("📰✨ AI Summarizer App")

# Sidebar mode selection
mode = st.sidebar.radio("Choose Mode:", ["Text Summarizer", "News Summarizer"])

# API key input
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if not api_key:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to continue.")
else:
    # Setup Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    # === TEXT SUMMARIZER ===
    if mode == "Text Summarizer":
        st.header("📝 Text Summarizer")
        user_text = st.text_area("Paste your text here:", height=200)
        length = st.radio("Summary length:", ["Short", "Medium", "Long"], index=1)

        if st.button("Summarize Text"):
            if not user_text.strip():
                st.error("⚠️ Please paste some text.")
            else:
                summary = summarize_text(model, user_text, length)
                st.subheader("📄 Summary:")
                st.write(summary)

    # === NEWS SUMMARIZER ===
    elif mode == "News Summarizer":
        st.header("📰 News Summarizer")

        # Categories
        categories = ["Technology", "Sports", "Crime", "Weather", "Business", "Health", "Entertainment"]
        selected_category = st.selectbox("Choose a news category:", categories)
        num_articles = st.slider("Number of Articles", 3, 10, 5)

        if st.button("Fetch & Summarize News"):
            news_articles = fetch_news(selected_category.lower(), NEWS_API_KEY, page_size=num_articles)

            if not news_articles:
                st.warning("⚠️ No news found. Try another category.")
            else:
                scored_articles = []
                for art in news_articles:
                    summary, score = summarize_and_score(art, model, selected_category)
                    scored_articles.append({**art, "summary": summary, "score": score})

                # Sort articles by score (optional)
                scored_articles = sorted(scored_articles, key=lambda x: x["score"], reverse=True)

                st.subheader(f"📌 {len(scored_articles)} {selected_category} News Summaries")
                for i, art in enumerate(scored_articles, 1):
                    st.markdown(f"### {i}. 📰 [{art['title']}]({art['url']}) (Score: {art['score']})")
                    if art.get("image"):
                        st.image(art["image"], width=500)
                    st.write(art["summary"])
                    st.caption(f"Published at: {art['publishedAt']}")
                    st.markdown("---")