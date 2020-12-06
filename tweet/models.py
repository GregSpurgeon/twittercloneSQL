from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, related_name="user", on_delete=models.CASCADE)
    message = models.TextField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.message} - {self.user}'
