from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()

    image = models.URLField(help_text='(Copy Image Address)', blank=True)
    content = models.TextField()

    class Meta: 
        ordering = ['-pub_date']
    
    categories = (
        ('FUN', 'Fun'),
        ('MUSIC', 'Music'),
        ('MOVIES', 'Movies'),
        ('EDUCATION', 'Education'),
        ('SCIENCE', 'Science'),
        ('TECHNOLOGY', 'Technology'),
        ('ANIMALS', 'Animals'),
        ('FOOD', 'Food'),
    )
    category = models.CharField(max_length=200, choices = categories, default='news')

    # def get_absolute_url(self):
    #     return reverse('story')


# categories = [('fun', 'fun'), ('music', 'music'), ('movies', 'movies'), ('education', 'education'), ('science', 'science'), ('technology', 'technology'), ('animals', 'animals'), ('food', 'food')]