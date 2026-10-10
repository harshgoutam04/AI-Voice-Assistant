# 🎙️ AI Voice Assistant

An AI-powered Voice Assistant built using **Streamlit**, **Groq Whisper**, **Groq LLM**, and **Edge-TTS**.

The application allows users to speak naturally through their microphone, converts speech into text, generates intelligent responses using an LLM, and converts those responses back into natural-sounding speech.

---

## 🚀 Features

- 🎤 Voice Input using Streamlit Audio Recorder
- 📝 Speech-to-Text using Groq Whisper
- 🤖 AI Responses using Groq llm
- 🔊 Text-to-Speech using Microsoft Edge-TTS
- 💬 Multi-turn Conversation Memory
- 🧹 Clear Conversation Option
- ⚡ Fast Response Generation
- 🌐 Ready for Deployment with Streamlit

---

## 🏗️ Architecture

```
                 User
                  │
                  ▼
         🎤 Voice Input
                  │
                  ▼
      Groq Whisper (Speech-to-Text)
                  │
                  ▼
          User Transcript
                  │
                  ▼
              Groq LLM
                  │
                  ▼
           AI Response
                  │
                  ▼
      Edge-TTS (Text-to-Speech)
                  │
                  ▼
          🔊 Audio Response
```

---

## 📁 Project Structure

```
Voice-AI-Bot/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── assets/
│   └── temp/
│
├── services/
│   ├── stt.py
│   ├── llm.py
│   ├── tts.py
│   └── audio_utils.py
│
└── README.md
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Speech-to-Text

- Groq Whisper API

### Large Language Model

- Groq LLM

### Text-to-Speech

- Microsoft Edge-TTS

### Other Libraries

- Groq Python SDK
- python-dotenv
- Streamlit
- Edge-TTS

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Voice-AI-Bot.git

cd Voice-AI-Bot
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## Environment Variables

### Local Development

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key

LLM_MODEL=openai/gpt-oss-120b

STT_MODEL=whisper-large-v3-turbo

VOICE_NAME=en-US-AriaNeural
```

### Streamlit Cloud Deployment

Do not commit `.env` or your API key to GitHub. In your Streamlit Cloud app:

1. Open the app's **Settings** menu.
2. Select **Secrets**.
3. Add the following TOML:

```toml
GROQ_API_KEY = "your_new_groq_api_key"
```

4. Save the secret and restart/redeploy the app.

The application reads `GROQ_API_KEY` from Streamlit Secrets in the cloud and
continues to support `.env` for local development.

---

## Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📸 Workflow

1. Click the microphone.
2. Speak naturally.
3. Audio is sent to Groq Whisper.
4. Speech is converted to text.
5. Transcript is sent to Groq LLM.
6. AI generates a response.
7. Edge-TTS converts the response into speech.
8. Audio is played back to the user.

---

## Future Improvements

- Real-time streaming conversations
- Automatic audio playback
- Multiple voice selections
- Voice interruption support
- WebSocket-based communication
- React + FastAPI frontend
- Multi-language support
- Voice activity detection
- Conversation summaries

---

## Author

**Harsh Vardhan Goutam**

AI/ML Engineer

GitHub: https://github.com/harshgoutam04

LinkedIn: https://www.linkedin.com/in/harsh-goutam-506414307/

---

## License

This project is developed for educational and demonstration purposes.