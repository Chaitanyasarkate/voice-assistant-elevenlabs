# Voice Virtual Assistant (ElevenLabs + Python)

This proof‑of‑concept project shows how to build a simple voice‑activated AI assistant in Python using:

- **SpeechRecognition** for microphone input
- **OpenAI (ChatGPT)** or simple rule‑based logic for responses
- **ElevenLabs** for text‑to‑speech with realistic voices
- **PyAudio** for audio I/O

The assistant listens for your voice, converts speech to text, generates a reply and speaks the answer back.

---

## Features

- 🎤 Voice input through your system microphone
- 🧠 Basic command processing (`hello`, `time`, etc.)
- 🤖 Optional ChatGPT integration for free‑form replies
- 🔉 Realistic voice output via ElevenLabs
- 🚪 Say "exit" / "quit" / "goodbye" to stop

> Advanced enhancements you can add:
>
> - Wake‑word detection (`Hey assistant`)
> - Weather API, calendar lookups, open apps, smart‑home control
> - GUI with Streamlit, Kivy or Tkinter
> - Logging, error handling and retries
> - Hot‑key / system tray utility

---

## Installation

1. **Clone this repository** (or copy the files into a folder).

2. **Create a Python virtual environment** (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

   The `requirements.txt` now includes `google-generative-ai` if you plan
   on using Gemini. If you don't need it you may remove that line.

   > ⚠️ Make sure to run the command on its own line. In the earlier transcript
   > it was accidentally combined with the `setx` command, which caused the
   > `No such file or directory` error.

4. **Obtain API keys**
   - **ElevenLabs:** <https://elevenlabs.io> → Profile → API keys
   - **OpenAI:** <https://platform.openai.com> (optional for ChatGPT replies)

- **Google Gemini:** Obtain a Generative AI API key via Google Cloud if you prefer to use Gemini instead of/dovetail with OpenAI

1. **Configure keys**
   - Set environment variables (Windows PowerShell example):

     ```powershell
     setx ELEVENLABS_API_KEY "your_elevenlabs_key"
     setx OPENAI_API_KEY "your_openai_key"   # optional (used when GOOGLE_API_KEY is not set)
     setx GOOGLE_API_KEY "your_google_gemini_key"  # optional, use instead of OpenAI
     ```

   - Alternatively, you can edit `config.py` and hard‑code the values (not recommended).

---

## Usage

Run the assistant from the workspace root:

```powershell
python main.py
```

Speak into your microphone. Here are some sample commands:

- “Hello” → assistant greets you.
- “What time is it?” → tells the current system time.
- “What’s the weather?” → placeholder response (customise with a weather API).
- “Tell me a joke” → if OpenAI key provided, the model will answer.
- “Exit” / “Quit” / “Goodbye” → assistant says goodbye and stops.

---

## Project Structure

```
voice-assistant/
├── main.py         # entry point
├── config.py       # helper for API keys
├── requirements.txt
└── README.md
```

---

## Notes

- **Microphone permissions**: make sure your system allows Python to access the mic.
- **PyAudio issues on Windows**: if installation fails, install the wheel from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
- **ElevenLabs voices**: change the `voice` parameter in `speak()` or explore the API for additional options.

Happy coding! 🎧💬
