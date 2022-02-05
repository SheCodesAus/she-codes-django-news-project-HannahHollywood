# Step 9. Create urls.py & create URLS for User App
from django.urls import path
from .views import CreateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
]