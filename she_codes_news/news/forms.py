from django import forms
from django.forms import ModelForm
from .models import NewsStory

# ABOVE Step 1. Create a forms.py and complete imports & add class

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']
        # Step 2. Add a date picker widget (Forms)
        wigets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }