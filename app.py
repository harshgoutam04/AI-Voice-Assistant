import streamlit as st
import os

from services.stt import SpeechToText
from services.llm import LLMService
from services.tts import TextToSpeech
from services.audio_utils import (
    save_uploaded_audio,
    clear_temp,
    get_response_audio_path,
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎙️",
    layout="wide",
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.block-container{
    max-width:950px;
    margin:auto;
}

.user-message{
    background:#DCF8C6;
    padding:15px;
    border-radius:15px;
    margin-bottom:12px;
}

.ai-message{
    background:#F1F0F0;
    padding:15px;
    border-radius:15px;
    margin-bottom:12px;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD SERVICES
# --------------------------------------------------

@st.cache_resource
def load_services():

    stt = SpeechToText()

    llm = LLMService()

    tts = TextToSpeech()

    return stt, llm, tts


stt, llm, tts = load_services()

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

if "last_audio" not in st.session_state:

    st.session_state.last_audio = None

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("Settings")


    st.divider()

    if st.button("Clear Conversation", use_container_width=True):

        st.session_state.messages = []

        st.session_state.last_audio = None

        clear_temp()

        st.rerun()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    "<div class='title'>🎙️ AI Voice Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Speak naturally with your AI Assistant</div>",
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# DISPLAY CHAT
# --------------------------------------------------

if len(st.session_state.messages):

    st.subheader("💬 Conversation")

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(
                f"""
<div class="user-message">

👤 <b>You</b>

<br><br>

{msg["content"]}

</div>
""",
unsafe_allow_html=True
)

        else:

            st.markdown(
                f"""
<div class="ai-message">

🤖 <b>Assistant</b>

<br><br>

{msg["content"]}

</div>
""",
unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# RECORD AUDIO
# --------------------------------------------------

st.subheader("🎤 Speak")

audio = st.audio_input("Tap the microphone and ask your question")

# --------------------------------------------------
# PROCESS AUDIO
# --------------------------------------------------

if audio is not None:

    try:

        # Clear previous temporary files
        clear_temp()

        # -----------------------------
        # Save recorded audio
        # -----------------------------

        with st.spinner("🎤 Saving your voice..."):

            audio_path = save_uploaded_audio(audio)

        # -----------------------------
        # Speech To Text
        # -----------------------------

        with st.spinner("📝 Understanding your speech..."):

            transcript = stt.transcribe(audio_path)

        if transcript.strip() == "":

            st.error("Sorry, I couldn't understand what you said.")

            st.stop()

        # Show transcript

        with st.chat_message("user"):

            st.write(transcript)

        # Save user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": transcript
            }
        )

        # -----------------------------
        # AI Thinking
        # -----------------------------

        with st.spinner("🤖 Thinking..."):

            ai_response = llm.generate(
                st.session_state.messages
            )

        # Show response

        with st.chat_message("assistant"):

            st.write(ai_response)

        # Save AI response

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

        # -----------------------------
        # Text To Speech
        # -----------------------------

        with st.spinner("🔊 Generating voice..."):

            response_audio = get_response_audio_path()

            audio_file = tts.generate_audio(
                ai_response,
                response_audio
            )

        # -----------------------------
        # Store Latest Audio
        # -----------------------------

        st.session_state.last_audio = audio_file

        st.success("✅ Response generated successfully!")

    except Exception as e:

        st.error(f"Error: {e}")

# --------------------------------------------------
# PLAY RESPONSE
# --------------------------------------------------

if st.session_state.last_audio:

    st.divider()

    st.subheader("🔊 Assistant Voice")

    with open(st.session_state.last_audio, "rb") as f:

        audio_bytes = f.read()

    st.audio(
        audio_bytes,
        format="audio/mp3"
    )

# --------------------------------------------------
# READY FOR NEXT QUESTION
# --------------------------------------------------

st.divider()

st.info(
    "🎤 Click the microphone again to continue the conversation."
)

st.caption(
    "Powered by Groq Whisper • Groq LLM • Edge-TTS"
)