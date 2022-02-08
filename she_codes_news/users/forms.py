# Step 3. Create Forms for User Login & Updates (User Apps)
from cgitb import html
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Valid email address required.')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2',]

# -----------------------

class CreateUserProfileForm(forms.Form):
    avatar = forms.URLField(initial='http://')
    location = forms.CharField(max_length=30)
    social_media_link = forms.URLField(initial='http://')
    bio = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Who are you? What do you like to write about?'
    )

    # def clean(self):
    #     cleaned_data = super(CreateUserProfileForm, self).clean()
    #     avatar = cleaned_data.get('avatar')
    #     location = cleaned_data.get('location')
    #     social_media_link = cleaned_data.get('social-link')
    #     bio = cleaned_data.get('bio')

    class Meta:
        model = CustomUser
        fields = ['avatar', 'location', 'social_media_link', 'bio',]

#  ----------------------

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']