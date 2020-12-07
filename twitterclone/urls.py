"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.views import index_view, SignUpView, FollowingView, UnfollowingView, UserPage
from authentication.views import login_view, logout_view
from tweet.views import create_tweet_view, tweets_view
from notification.views import notification_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="home"),
    path("signup/", SignUpView.as_view()),
    path("login/", login_view),
    path('logout/', logout_view),
    path('tweetform/', create_tweet_view),
    path('following/<int:user_id>/', FollowingView.as_view()),
    path('unfollowing/<int:user_id>/', UnfollowingView.as_view()),
    path('tweets/<int:tweet_id>/', tweets_view),
    path('user/<int:user_id>/', UserPage.as_view(), name='users_page'),
    path('notification/', notification_view),
]
