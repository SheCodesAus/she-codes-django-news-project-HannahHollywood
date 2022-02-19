from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.utils import timezone

# Create a forms.py and complete imports & add class
class StoryForm(forms.ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'category', 'content']
        widgets = {
            # BELOW did not work... but keeping to laugh at
            # 'category': forms.Select(categories=categories, attrs={'class': 'form-control'}),
        }
        # Add a date picker widget (Forms)
        # widgets = {
        #     'pub_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")