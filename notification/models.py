from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_mentioned = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    seen_message = models.BooleanField(default=False)
