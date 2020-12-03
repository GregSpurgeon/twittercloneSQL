from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TwitterUser(AbstractUser):
    display_name = models.CharField(blank=True, null=True, max_length=50)
