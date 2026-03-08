import streamlit as st
import google.generativeai as genai
from elevenlabs.client import ElevenLabs
from elevenlabs import play

ELEVENLABS_API_KEY = st.secrets["sk_77e56138817539e7fe2539901df3e634adfe79a0051e27f7"]
GOOGLE_API_KEY = st.secrets["AIzaSyCgRsgmfwOpSfOcNnhN76w8lwXLNADfaOw"]

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

eleven = ElevenLabs(api_key=ELEVENLABS_API_KEY)

st.title("Jarvis AI Voice Assistant")

user_input = st.text_input("Ask something")

if st.button("Ask"):

    response = model.generate_content(user_input)

    answer = response.text

    st.write("Assistant:", answer)

    audio = eleven.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        text=answer
    )

    play(audio)
