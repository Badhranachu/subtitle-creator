import whisper
import os

VIDEO_FILE = "videos/VideoProject.mp4"  # change if needed
LANGUAGE = "en"

def seconds_to_vtt_time(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:06.3f}"

model = whisper.load_model("base")

print("Transcribing...")
result = model.transcribe(VIDEO_FILE, language=LANGUAGE, verbose=True)

output_file = VIDEO_FILE.replace(".mp4", ".vtt")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("WEBVTT\n\n")

    for s in result["segments"]:
        start = seconds_to_vtt_time(s["start"])
        end = seconds_to_vtt_time(s["end"])
        text = s["text"].strip()

        f.write(f"{start} --> {end}\n")
        f.write(f"{text}\n\n")

print("Subtitle saved:", output_file)
