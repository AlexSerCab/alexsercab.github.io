"""
Local AI Courtroom Transcription System
Used in Poder Judicial Tamaulipas - Sala Oralidad Penal
Stack: Whisper (openai-whisper), Python, pydub
Author: Alejandro Serna Cabrera
"""
import whisper
import os
from datetime import datetime
from pydub import AudioSegment

MODEL_SIZE = "medium"  # small/medium/large for Spanish accuracy

def transcribe_audiencia(audio_path, output_dir="./transcripciones"):
    os.makedirs(output_dir, exist_ok=True)
    print(f"[+] Cargando modelo Whisper {MODEL_SIZE}...")
    model = whisper.load_model(MODEL_SIZE)
    
    # Convert to wav if needed
    if not audio_path.endswith(".wav"):
        audio = AudioSegment.from_file(audio_path)
        wav_path = os.path.splitext(audio_path)[0] + ".wav"
        audio.export(wav_path, format="wav")
        audio_path = wav_path

    print(f"[+] Transcribiendo: {audio_path}")
    result = model.transcribe(audio_path, language="es", fp16=False)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    out_txt = os.path.join(output_dir, f"{base_name}_{timestamp}.txt")
    
    with open(out_txt, "w", encoding="utf-8") as out:
        out.write(f"Audiencia: {base_name}\nFecha: {timestamp}\n")
        out.write("-"*40 + "\n")
        out.write(result["text"])
    
    print(f"[OK] Transcripcion guardada en {out_txt}")
    return out_txt

if __name__ == "__main__":
    # Ejemplo: python transcription_local.py audiencia_123.mp3
    import sys
    if len(sys.argv) < 2:
        print("Uso: python transcription_local.py <audio_file>")
    else:
        transcribe_audiencia(sys.argv[1])