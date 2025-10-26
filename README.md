# Text Summarizer using Transformers

This project uses a pre-trained transformer model (`facebook/bart-large-cnn`) from Hugging Face to generate concise summaries of long text inputs. It’s designed for quick testing, learning NLP pipelines, and showcasing foundational AI skills.

# Features
- Summarizes long text into short, readable output
- Uses Hugging Face’s `pipeline("summarization")`
- Adjustable summary length (`max_length`, `min_length`)
- Deterministic output with `do_sample=False`
- Beginner-friendly CLI interface

# Tech Stack
- Python
- Hugging Face Transformers
- Pre-trained BART model

# Installation
- pip install transformers
