from django import forms

class ParagraphForm(forms.Form):
    input_paragraph = forms.CharField(widget=forms.Textarea, label='Enter Marathi Paragraph')
    output_paragraph = forms.CharField(widget=forms.Textarea, required=False, label='Summarized Paragraph', disabled=True)
