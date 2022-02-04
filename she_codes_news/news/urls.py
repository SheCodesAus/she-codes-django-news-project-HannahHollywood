from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Step 13. Use the view in the URLS
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    # Step 1. Add the form for newStory in the urls (Forms)
    path('add-story/', views.AddStoryView.as_view(), name='newStory')
]
