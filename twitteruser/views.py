from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from twitteruser.forms import SignUpForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from django.views.generic import View
# Create your views here.


@login_required
def index_view(request):
    home = 'index.html'
    twitteruser = TwitterUser.objects.filter(id=request.user.id).first()
    tweet = Tweet.objects.filter(user=request.user)
    users_followers = TwitterUser.objects.get(username=request.user).following.all()
    for follower in users_followers:
        followers_tweets = Tweet.objects.filter(user=follower)
        tweet = tweet | followers_tweets
    tweet = tweet.order_by('-created_at')

    return render(request, home, {"twitteruser": twitteruser,
                                  "tweets": tweet,
                                  "users_followers": users_followers})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "sign_up_form.html", {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name']
            )
            return redirect("/")


class FollowingView(View):
    def get(self, request, user_id):
        logged_in_user = TwitterUser.objects.get(username=request.user)
        following_user = TwitterUser.objects.get(id=user_id)
        logged_in_user.following.add(following_user)
        logged_in_user.save()
        return redirect('/')


class UnfollowingView(View):
    def get(self, request, user_id):
        logged_in_user = TwitterUser.objects.get(username=request.user)
        following_user = TwitterUser.objects.get(id=user_id)
        logged_in_user.following.remove(following_user)
        logged_in_user.save()
        return redirect('/')


class UserPage(View):
    def get(self, request, user_id):
        curr_user = TwitterUser.objects.get(id=user_id)
        tweets = Tweet.objects.filter(user=user_id).order_by('-created_at')
        total_tweets = Tweet.objects.filter(user=user_id).count()
        following_total = TwitterUser.objects.filter(following=user_id).count()
        users_followers = TwitterUser.objects.get(username=request.user).following.all().count()
        return render(request, 'user_page.html',
                               {'user': curr_user,
                                'tweets': tweets,
                                'total': total_tweets,
                                'following_total': following_total,
                                'user_followers': users_followers})
