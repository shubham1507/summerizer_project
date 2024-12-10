from django.shortcuts import render
from django.http import JsonResponse
from .forms import ParagraphForm
import re

def is_marathi(text):
    """Check if the given text is Marathi"""
    return bool(re.search(r'[\u0900-\u097F]', text))  # Marathi Unicode range

def summarize_paragraph(paragraph):
    """Summarize the paragraph to 60% of its length by sentence count."""
    # Split paragraph into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)
    
    # Calculate the number of sentences to retain (60% of the original length)
    num_sentences = len(sentences)
    num_sentences_to_keep = max(1, int(num_sentences * 0.6))  # Ensure at least one sentence
    
    # Take the first num_sentences_to_keep sentences
    summarized = '. '.join(sentences[:num_sentences_to_keep]) + ('.' if num_sentences_to_keep > 0 else '')
    
    return summarized

def index(request):
    form = ParagraphForm()

    if request.method == 'POST':
        input_text = request.POST.get('input_paragraph', '')
        if not is_marathi(input_text):
            return JsonResponse({'error': 'Please enter a Marathi paragraph.'})

        summarized_text = summarize_paragraph(input_text)
        form = ParagraphForm(initial={'input_paragraph': input_text, 'output_paragraph': summarized_text})

    return render(request, 'summerizer/index.html', {'form': form})
