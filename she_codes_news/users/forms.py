# Step 3. Create Forms for User Login & Updates (User Apps)
from cgitb import html
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, CreateUserProfileForm
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
    social_link = forms.CharField(max_length=30)
    bio = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Tell us about yourself!'
    )
    # source = forms.CharField(       # A hidden input for internal use
    #     max_length=50,              # tell from which page the user sent the message
    #     widget=forms.HiddenInput()
    # )

    def clean(self):
        cleaned_data = super(CreateUserProfileForm, self).clean()
        social_link = cleaned_data.get('social-link')
        bio = cleaned_data.get('bio')
        if not social_link and not bio:
            raise forms.ValidationError('You have to write something!')

    class Meta:
        model = CustomUser
        fields = ['social_link', 'bio',]

#  ----------------------

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']