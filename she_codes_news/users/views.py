from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, EditUserProfileForm
from news.models import NewsStory

# -------------------------------------------------------------------
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:editProfile')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        f=super().form_valid(form)
        user = self.object
        login(self.request, user)
        return f

class EditUserProfileView(UpdateView):
    form_class = EditUserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/editProfile.html'
    
    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:profile', kwargs={"pk":self.request.user.id})

    def get_object(self):
        return self.request.user

# --------------------------------------------------------------------

# Display the Custom User Profile page
class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfileHome.html'
