import os
import yt_dlp
import google.generativeai as genai

MAX_DURATION_SECONDS = 600
AUDIO_DIR = './audio'
PROMPT = "Summarize this audio"
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def download_audio(url: str) -> str | None:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{AUDIO_DIR}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            duration = info_dict.get('duration', 0)

            if duration > MAX_DURATION_SECONDS:
                print(f"Video exceeds the maximum duration limit of {MAX_DURATION_SECONDS // 60} minutes.")
                return None

            ydl.download([url])
            title = info_dict.get("title", "audio")
            path = f"{AUDIO_DIR}/{title}.mp3"
            return path
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None


def upload_audio_file(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Audio file not found: {path}")
    try:
        return genai.upload_file(path=path)
    except Exception as e:
        print(f"Error uploading audio file: {e}")
        return None


def summarize(url: str) -> str:
    path = download_audio(url)
    if path is None:
        return "The audio could not be processed due to duration limits or download errors."

    audio_file = upload_audio_file(path)
    if audio_file is None:
        return "Failed to upload audio file."

    try:
        response = model.generate_content([PROMPT, audio_file])
        return response.text if response else "No summary generated."
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Error generating summary."