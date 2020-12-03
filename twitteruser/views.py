from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from twitteruser.forms import LoginForm, SignUpForm
from twitteruser.models import TwitterUser
# Create your views here.


def index_view(request):
    home = 'index.html'
    twitteruser = TwitterUser.objects.filter(id=request.user.id).first()
    return render(request, home, {"twitteruser": twitteruser})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next',
                                    reverse('home')))
    form = LoginForm()
    return render(request, 'login_form.html', {"form": form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name']
            )
            return redirect("/")
    form = SignUpForm()
    return render(request, "sign_up_form.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
