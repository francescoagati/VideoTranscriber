# OBS Recording Transcriber

Process OBS recordings or any video/audio files with AI-based transcription and summarization locally on your machine.


## Features
- AI transcription using Whisper.
- Summarization using Hugging Face Transformers.
- File selection, resource validation, and error handling.

## Installation
1. Clone the repo.
git clone [https://github.com/DataAnts-AI/VideoTranscriber.git
cd VideoTranscriber
2. Install dependencies:
 pip install -r requirements.txt


Notes:
Ensure that the versions align with the features you use and your system compatibility.
torch version should match the capabilities of your hardware (e.g., CUDA support for GPUs).
whisper might need to be installed from source or a GitHub repository if it's not available on PyPI.
If you encounter any issues regarding compatibility, versions may need adjustments.

3. streamlit run app.py
