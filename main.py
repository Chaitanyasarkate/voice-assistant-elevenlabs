import sys
import datetime
import speech_recognition as sr

from elevenlabs.client import ElevenLabs
from elevenlabs import play

import google.generativeai as genai

from config import ELEVENLABS_API_KEY, GOOGLE_API_KEY

# -----------------------------
# Initialize APIs
# -----------------------------

if not ELEVENLABS_API_KEY or ELEVENLABS_API_KEY.startswith("YOUR"):
    print("Please add your ElevenLabs API key in config.py")
    sys.exit(1)

eleven = ElevenLabs(api_key=ELEVENLABS_API_KEY)

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
else:
    model = None

recognizer = sr.Recognizer()

# -----------------------------
# Listen Function
# -----------------------------

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except:
        print("Could not understand audio")
        return ""


# -----------------------------
# Speak Function
# -----------------------------

def speak(text):

    audio = eleven.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        text=text
    )

    play(audio)


# -----------------------------
# Ask Gemini
# -----------------------------

def ask_gemini(prompt):

    if not model:
        return "AI service not configured."

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("Gemini error:", e)
        return "Error contacting AI service."


# -----------------------------
# Command Processing
# -----------------------------

def process_command(cmd):

    if "hello" in cmd:
        return "Hello! How can I help you?"

    elif "time" in cmd:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}"

    elif "exit" in cmd or "quit" in cmd:
        return "Goodbye!"

    else:
        return ask_gemini(cmd)


# -----------------------------
# Main Loop
# -----------------------------

def main():

    print("Voice Assistant Started")

    while True:

        command = listen()

        if not command:
            continue

        response = process_command(command)

        speak(response)

        if "exit" in command or "quit" in command:
            break


if __name__ == "__main__":
    main()