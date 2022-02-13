from django import forms
from django.forms import ModelForm
from .models import NewsStory

# Create a forms.py and complete imports & add class

class StoryForm(forms.ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content']
        # Add a date picker widget (Forms)
        widgets = {
            'pub_date': forms.DateInput(format=('%d/%m/%Y'), 
    attrs={'class': 'form-control', 'placeholder': 'Select a date', 
    'type': 'date'}),
        }