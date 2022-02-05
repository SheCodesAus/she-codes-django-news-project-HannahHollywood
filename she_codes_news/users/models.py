from django.contrib.auth.models import AbstractUser

# Step 2. Create your models here (User Apps)
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username