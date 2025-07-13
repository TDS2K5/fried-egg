# FriedEgg - Sunny side up AI assistant

FriedEgg is a Tony Stark inspired, voice+text-based virtual assistant designed to perform tasks such as web
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

- Set your own API keys for Gemini and NewsAPI, can be hardcoded for personal use.

---

**Usage** :

```bash
python3 main.py
```

**Project Structure** :

- main.py - Runs text-based mode by default. Voice code is included but commented out.
- dev.py - for testing in DEV mode.
- musicLibrary.py - a dictionary containing songs mapped to YouTube links, customizable by user. It is imported as a module in main.py
- test.py - used to test mic input mainly in Linux machines.

---

**Contributions** :

- Pull requests are welcome.
- Help required for voice input mode.
- For related questions you can email me at tanishkputhran1@gmail.com

**Notes** :

- Voice activated mode unstable on Linux, hence text-based is set to default.
- Issues with mic input on Linux machines to be fixed in future commits.
