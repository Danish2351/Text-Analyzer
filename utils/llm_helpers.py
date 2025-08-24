import google.generativeai as genai
from groq import Groq
from config import GEMINI_API_KEY, GROQ_API_KEY

# --- Gemini ---
genai.configure(api_key=GEMINI_API_KEY)

def summarize_gemini(text: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(f"Summarize this text:\n{text}")
    return response.text

# --- Groq (Mistral) ---
groq_client = Groq(api_key=GROQ_API_KEY)

def summarize_groq(text: str) -> str:
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Summarize this text:\n{text}"}],
        max_tokens=300
    )
    return response.choices[0].message.content
