from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView
from .models import NewsStory, get_user_model
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

# Add a view for a single story
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# Add ability to create a new story
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Add ability to edit a story
class EditStoryView(UpdateView):
    model = NewsStory
    template_name = 'news/editStory.html'
    fields = ['title', 'pub_date', 'image', 'category', 'content']
    success_url = reverse_lazy('news:index')

# Add ability to delete a story
class DeleteStoryView(DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')