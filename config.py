"""Configuration helpers for the assistant.

Keys are pulled from environment variables by default.  You can override
by editing the values directly, but don't commit secrets to source control.
"""

import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "sk_77e56138817539e7fe2539901df3e634adfe79a0051e27f7")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyCgRsgmfwOpSfOcNnhN76w8lwXLNADfaOw")  # Gemini / Generative AI API key or empty
