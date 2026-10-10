import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq Models
LLM_MODEL = "openai/gpt-oss-120b"
STT_MODEL = "whisper-large-v3"

# Edge TTS Voice
VOICE_NAME = "en-US-AriaNeural"