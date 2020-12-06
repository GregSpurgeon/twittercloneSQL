from django.shortcuts import render, redirect
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
import re
# Create your views here.


def create_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posted_tweet = Tweet.objects.create(
              user=request.user,
              message=data['message'],
            )
            mentioned_users = re.findall('@([a-zA-Z0-9_]*)', data['message'])
            if mentioned_users:
                for mentioned_user in mentioned_users:
                    matched_user = TwitterUser.objects.get(username=mentioned_user)
                    if matched_user:
                        Notification.objects.create(
                            user_mentioned=matched_user,
                            tweet=posted_tweet,
                        )
            return redirect("/")
    form = TweetForm()
    return render(request, "create_tweet_form.html", {'form': form})


def tweets_view(request, tweet_id):
    return render(request, 'tweets.html', {"tweets": Tweet.objects.filter(id=tweet_id)[::-1]})


