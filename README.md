# XTTS FastAPI TTS Service 🎤

This is a simple Text-to-Speech (TTS) API built using FastAPI and Coqui XTTS v2.

It converts text into speech and supports voice cloning using a reference audio file.

---

## Features

- Text to Speech API
- Multilingual support (Hindi, English, etc.)
- Voice cloning using `clean.wav`
- Streaming audio response

---

## Requirements

- Python 3.10
- 8GB RAM recommended

---

## ⚙️ Setup

###  1 Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```
### 2 Install dependencies
```bash
pip install -r requirements.txt
```
 ###  3 Run the Server
 ```bash
uvicorn tts_server:app --reload

