import streamlit as st
from utils.llm_helpers import summarize_gemini, summarize_groq
from utils.tokenizer_helpers import tokenize_text
from config import COSTS

st.set_page_config(page_title="Text Analysis Tool", layout="wide")

st.title("Text Analysis Tool")

# Input
user_text = st.text_area("Enter text to summarize", height=200)

if st.button("Analyze"):
    if not user_text.strip():
        st.warning("Please enter some text!")
    else:
        with st.spinner("Summarizing..."):
            try:
                # Summaries
                gemini_summary = summarize_gemini(user_text)
                groq_summary = summarize_groq(user_text)

                # Tokenization
                token_info = tokenize_text(user_text)

                # Cost estimation
                gemini_cost = token_info["bert_count"] * COSTS["gemini"]

                # Display
                st.subheader("📌 Summaries")
                col1, col2 = st.columns(2)
                col1.markdown("**Gemini Summary:**")
                col1.write(gemini_summary)
                col2.markdown("**Groq Summary:**")
                col2.write(groq_summary)

                st.subheader("🔤 Tokenization")
                st.json(token_info)

                st.subheader("Cost Estimation")
                st.write(f"Gemini : {token_info['bert_count']} tokens ≈ ${gemini_cost:.6f}")

            except Exception as e:
                st.error(f"Error: {e}")
