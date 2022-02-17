from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('story')

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=255)
    image = models.URLField(blank=True)
    content = models.TextField()
    class Meta: 
        ordering = ['-pub_date']

    # def get_absolute_url(self):
    #     return reverse('story')
