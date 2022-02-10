from django.shortcuts import render, redirect

#Step 9. Create 'view' for account page app (User App)
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views import generic
from django.views.generic.detail import DetailView
from .models import CustomUser
from .forms import CustomUserCreationForm, CreateUserProfileForm

# -------------------------------------------------------------------
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:createProfile')
    template_name = 'users/createAccount.html'

class CreateUserProfileView(FormView):
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('users:profileHome')
    template_name = 'users/createProfile.html'

# --------------------------------------------------------------------

# Display the Custom User Profile page
class UserProfileView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:profileHome')
    template_name = 'users/userProfileHome.html'