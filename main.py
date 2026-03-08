import streamlit as st
import google.generativeai as genai
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = st.secrets["ELEVENLABS_API_KEY"]
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

# Updated model
model = genai.GenerativeModel("gemini-1.5-flash")

eleven = ElevenLabs(api_key=ELEVENLABS_API_KEY)

st.title("AI Voice Assistant")

user_input = st.text_input("Ask something")

if st.button("Ask"):

    if user_input.strip():

        response = model.generate_content(user_input)

        answer = response.text

        st.write("Assistant:", answer)

    else:
        st.warning("Please enter a question")
