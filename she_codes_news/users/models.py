from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.URLField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    social_media_link = models.URLField(blank=True)
    bio = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.username