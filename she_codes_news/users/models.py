from django.contrib.auth.models import AbstractUser

# Step 2. Create your models here (User Apps)
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username




# from django.contrib.auth import get_user_model
# from django.db import models


# class NewsStory(models.Model):
#     title = models.CharField(max_length=200)
#     # author = models.CharField(max_length=200)
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE
#     )
#     pub_date = models.DateTimeField()
#     content = models.TextField()
