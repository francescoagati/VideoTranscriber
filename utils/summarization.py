from transformers import pipeline

SUMMARY_MODEL = "Falconsai/text_summarization"

def summarize_text(text):
    """Summarize text using a Hugging Face pipeline."""
    summarizer = pipeline("summarization", model=SUMMARY_MODEL)
    return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]
