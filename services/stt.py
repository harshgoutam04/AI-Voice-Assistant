"""
Speech-to-Text Service using Groq Whisper API
"""

import os
from groq import Groq
from config import GROQ_API_KEY, STT_MODEL


class SpeechToText:
    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=GROQ_API_KEY)

    def transcribe(self, audio_file_path: str) -> str:
        """
        Transcribe an audio file using Groq Whisper.

        Args:
            audio_file_path (str): Path to audio file

        Returns:
            str: Transcript
        """

        try:
            with open(audio_file_path, "rb") as audio_file:

                transcription = self.client.audio.transcriptions.create(
                    file=(os.path.basename(audio_file_path), audio_file.read()),
                    model=STT_MODEL,
                    response_format="verbose_json",
                    language="en"
                )

            return transcription.text

        except Exception as e:
            print(f"\nSTT Error: {e}")
            return ""