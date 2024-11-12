# YouTube Video Summarizer

This project allows users to download audio from YouTube videos, process them using Google Generative AI, and generate text summaries. It is designed to be simple and easy to use, and aims to help users quickly summarize the content of YouTube videos.

## Features

- Download audio from YouTube videos in MP3 format.
- Automatically check if the video exceeds a set duration limit (10 minutes by default).
- Upload the audio to Google Generative AI and generate a summary.
- Customizable duration limit to filter long videos.
  
## Requirements

- Python 3.12 or later.
- A Google API key with access to Google Generative AI.
- `yt-dlp` for downloading YouTube videos.
- `google-generativeai` library for interacting with Google Generative AI.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lindolfomoizinho/yt_brief.git
   cd yt_brief
   ```
2. Create a virtual environment:
    ```bash
    python -m venv .venv
     ```
3. Activate the virtual environment:
   - On Windows:
    ```bash
    .venv\Scripts\activate
    ```
   - On macOS/Linux:
   ```bash
    source .venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Set up your Google API key: Replace YOUR_API_KEY in the code with your actual API key for Google Generative AI.
6. Run the app: You can now use the summarize function to download and summarize YouTube videos. Example usage:
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/summarize/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DjQI0bsCtdws' \
    -H 'accept: application/json'
