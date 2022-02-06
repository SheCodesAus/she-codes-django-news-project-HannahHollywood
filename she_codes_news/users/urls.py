# Step 9. Create urls.py & create URLS for User App
from django.urls import path
from .views import CreateAccountView, CreateUserProfileView, UserProfileView
from django.views.generic.detail import DetailView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # Linking create-account page with the next page, which is create-profile
    path('create-profile/', CreateUserProfileView.as_view(), name='createProfile'),
    # Directing the create-profile page to the users completed profile
    path('profile-home/', UserProfileView.as_view(), name='profileHome')
]