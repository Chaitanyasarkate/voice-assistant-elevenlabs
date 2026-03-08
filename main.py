import streamlit as st
import google.generativeai as genai
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = st.secrets["ELEVENLABS_API_KEY"]
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

eleven = ElevenLabs(api_key=ELEVENLABS_API_KEY)

st.title("AI Voice Assistant")

user_input = st.text_input("Ask something")

if st.button("Ask"):

    if not user_input.strip():
        st.warning("Please enter a question")
    
    else:
        try:
            response = model.generate_content(user_input)

            answer = response.text

            st.write("Assistant:", answer)

        except Exception as e:
            st.error("AI service error. Please try again.")
            st.text(e)
