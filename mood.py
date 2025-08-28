# mood_detector_app.py

import streamlit as st
from transformers import pipeline

# Load sentiment analysis model from HuggingFace
sentiment_pipeline = pipeline("sentiment-analysis")

st.set_page_config(page_title="AI Mood Detector", page_icon="😀", layout="centered")

st.title("😀 AI Mood Detector (Emoji Generator)")
st.write("Type how you feel, and I’ll guess your mood!")

# --- User Input ---
user_text = st.text_area("How are you feeling today?")

if st.button("Detect Mood"):
    if user_text.strip():
        with st.spinner("Analyzing mood..."):
            result = sentiment_pipeline(user_text)[0]
            label = result['label']
            
            # Map mood to emojis
            emoji_map = {
                "POSITIVE": "😊",
                "NEGATIVE": "😢",
                "NEUTRAL": "😐"
            }
            emoji = emoji_map.get(label, "🤔")
            
            st.success(f"Detected Mood: **{label}** {emoji}")
    else:
        st.warning("⚠️ Please type something first.")
