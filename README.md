# FriedEgg - Sunny side up AI assistant

FriedEgg is a Tony Stark inspired, voice-activated cum text-based virtual assistant designed to perform tasks such as web
browsing, playing music, fetching news, and responding to user queries, powered by Google Gemini 2.5-flash model.

---

**Features** :

- Voice-activated command recognition
- Option to switch to text-based mode
- Opens websites like Google, YouTube, GitHub, etc.
- Plays music using a custom `musicLibrary.py`
- Fetches real-time news using NewsAPI
- Processes queries using Gemini 2.5-flash
- Replies back with pyttsx3
- Wake-word system for hands-free control

---

**Tech Stack** :

- ``Python 3.10+`
- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `requests`
- `google`
- `NewsAPI`
- `musicLibrary.py` (custom dictionary)

---

## 📦 Installation

> Python 3.10+ is recommended. Make sure `pip` is installed.

### Clone the repository

```bash
git clone https://github.com/TDS2K5/fried-egg
cd fried-egg
```

**Set up virtual environment** :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

<!-- Install dependencies :
```bash
pip install -r requirements.txt
``` -->

- Set your own API keys for Gemini and NewsAPI

**Usage** :

python3 main.py
(set to text-based mode by default)

**Troubleshooting** :

- Check device mic input using test.py

---

**Contributions** :

- Pull requests are welcome. Help required for voice input mode.

**Additional footnotes** :

- TTS voice activated mode still under development, hence text-based set to default.
- Issues with mic input on Linux machines to be fixed in future commits.
