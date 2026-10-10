"""
Audio Utility Functions
"""

import os
import shutil
import uuid
from pathlib import Path


TEMP_DIR = Path("assets/temp")


def ensure_temp_dir():
    """
    Create temp directory if it doesn't exist.
    """
    TEMP_DIR.mkdir(parents=True, exist_ok=True)


def clear_temp():
    """
    Delete all temporary audio files.
    """
    ensure_temp_dir()

    for file in TEMP_DIR.iterdir():
        if file.is_file():
            try:
                file.unlink()
            except Exception:
                pass


def save_uploaded_audio(uploaded_file):
    """
    Save Streamlit uploaded audio.

    Returns
    -------
    str
        Path of saved audio file.
    """

    ensure_temp_dir()

    filename = f"{uuid.uuid4()}.wav"

    filepath = TEMP_DIR / filename

    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    return str(filepath)


def get_response_audio_path():
    """
    Returns path where Edge-TTS should save output.
    """

    ensure_temp_dir()

    return str(TEMP_DIR / "response.mp3")