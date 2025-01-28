import whisper
from pathlib import Path
from transformers import pipeline, AutoTokenizer

WHISPER_MODEL = "base"
SUMMARIZATION_MODEL = "t5-base"

def transcribe_audio(audio_path: Path):
    """Transcribe audio using Whisper."""
    model = whisper.load_model(WHISPER_MODEL)
    result = model.transcribe(str(audio_path))
    transcript = result["text"]
    summary = summarize_text(transcript)
    return transcript, summary

def summarize_text(text):
    """Summarize text using a pre-trained T5 transformer model with chunking."""
    summarization_pipeline = pipeline("summarization", model=SUMMARIZATION_MODEL)
    tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL)
    
    max_tokens = 512
    
    tokens = tokenizer(text, return_tensors='pt')
    num_tokens = len(tokens['input_ids'][0])
    
    if num_tokens > max_tokens:
        chunks = chunk_text(text, max_tokens)
        summaries = []
        for chunk in chunks:
            summary_output = summarization_pipeline("summarize: " + chunk, max_length=150, min_length=30, do_sample=False)
            summaries.append(summary_output[0]['summary_text'])
        overall_summary = " ".join(summaries)
    else:
        overall_summary = summarization_pipeline("summarize: " + text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    
    return overall_summary

def chunk_text(text, max_tokens):
    """Splits the text into a list of chunks based on token limits."""
    tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL)
    words = text.split()
    
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        hypothetical_length = current_length + len(tokenizer(word, return_tensors='pt')['input_ids'][0]) - 2
        if hypothetical_length <= max_tokens:
            current_chunk.append(word)
            current_length = hypothetical_length
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(tokenizer(word, return_tensors='pt')['input_ids'][0]) - 2
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks