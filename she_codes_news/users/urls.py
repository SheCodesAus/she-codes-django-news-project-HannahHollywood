from django.urls import path
from .views import CreateAccountView, EditUserProfileView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # Linking create-account page with the next page, which is create-profile
    path('edit-profile/', EditUserProfileView.as_view(), name='editProfile'),
    # Directing the edit-profile page to the users completed profile
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]