from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

# -----------------------

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Valid email address required.')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2',]

# -----------------------

class EditUserProfileForm(forms.ModelForm):
    avatar = forms.URLField(help_text='Enter URL', required=False)
    location = forms.CharField(max_length=30, required=False)
    social_media_link = forms.URLField(help_text='Enter URL', required=False)
    bio = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        required=False,
        help_text='Who are you? What do you like to write about?'
    )

    class Meta:
        model = CustomUser
        fields = ['avatar', 'location', 'social_media_link', 'bio',]

#  ----------------------