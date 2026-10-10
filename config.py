import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
except FileNotFoundError:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq Models
LLM_MODEL = "openai/gpt-oss-120b"
STT_MODEL = "whisper-large-v3"

# Edge TTS Voice
VOICE_NAME = "en-US-AriaNeural"