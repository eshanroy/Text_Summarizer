from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input long text
text = input("Enter text to summarize:\n")

# Run summarization
summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

# Output result
print("\nSummary:\n", summary)