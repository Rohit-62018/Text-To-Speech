from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from TTS.api import TTS
import io
import os
import soundfile as sf

app = FastAPI()

print("Loading XTTS model...")
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    gpu=False
)
print("XTTS loaded ✔")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPEAKER_WAV = os.path.join(BASE_DIR, "clean.wav")

class TTSRequest(BaseModel):
    text: str
    language: str = "hi"

@app.post("/tts")
def tts_endpoint(req: TTSRequest):
    print("Language:", req.language)

    if not os.path.exists(SPEAKER_WAV):
        return JSONResponse(400, {"error": "clean.wav not found"})

    wav = tts.tts(
        text=req.text,
        speaker_wav=SPEAKER_WAV,
        language=req.language
    )

    sr = tts.synthesizer.output_sample_rate
    wav_io = io.BytesIO()
    sf.write(wav_io, wav, sr, format="WAV")
    wav_io.seek(0)

    def audio_stream():
        yield wav_io.read()

    return StreamingResponse(
        audio_stream(),
        media_type="audio/wav"
    )
