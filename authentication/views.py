from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from twitteruser.forms import LoginForm

# Create your views here.


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))