from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Use the view in the URLS
    path('story/<int:pk>', views.StoryView.as_view(), name='story'),
    # Add the form for newStory in the urls (Forms)
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # Add a way to edit a story
    path('story/<int:pk>/edit', views.EditStoryView.as_view(), name='editStory'),
    # Add a a way to delete a story
    path('story/<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
]
