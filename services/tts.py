"""
Text-to-Speech Service using Edge-TTS
"""

import asyncio
import os
import edge_tts

from config import VOICE_NAME


class TextToSpeech:

    def __init__(self):
        self.voice = VOICE_NAME

        # Create folder automatically if it doesn't exist
        os.makedirs("assets/temp", exist_ok=True)

    async def _generate(self, text: str, output_file: str):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice
        )

        await communicate.save(output_file)

    def generate_audio(
        self,
        text: str,
        output_file: str = "assets/temp/response.mp3"
    ):

        try:

            # Make sure folder exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            asyncio.run(
                self._generate(text, output_file)
            )

            return output_file

        except Exception as e:

            print(f"TTS Error: {e}")

            return None