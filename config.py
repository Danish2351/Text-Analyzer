import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Cost per 1K tokens (update if needed)
COSTS = {
    "gemini": 0.0000003,  # $0.00025 / token
}

# Safety check
if not GEMINI_API_KEY or not GROQ_API_KEY:
    raise ValueError("⚠️ API keys not found. Please set GEMINI_API_KEY and GROQ_API_KEY in .env file")
