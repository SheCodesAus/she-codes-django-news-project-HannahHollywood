from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CreateUserProfileForm
from news.models import NewsStory

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
class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfileHome.html'

def get_user_profile(request):
    user = request.user
    stories = NewsStory.objects.filter(author=request.user.id)
    return render(request, 'users/userProfileHome.html', {"user": request.user, "stories": stories})
