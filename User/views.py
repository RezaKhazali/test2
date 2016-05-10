from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from User.forms import *
from User.models import UserProfile
from User.models import *


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/profile")
        else:
            login_form = LoginForm(request.POST)
            register_form = RegistrationForm(request.POST)

    else:
        login_form = LoginForm
        register_form = RegistrationForm

    return render(request, "login.html", {
        'login_form': login_form,
        'register_form': register_form
    })


def register(request):
    if request.method == 'POST':
        print("method is post.")
        login_form = LoginForm(request.POST)
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = User()
            user.username = register_form.cleaned_data['username']
            user.set_password(register_form.cleaned_data['password'])
            user.email = register_form.cleaned_data['email']
            user.save()
            userprofile = UserProfile()
            userprofile.user = user
            userprofile.birthday = register_form.cleaned_data['birthday']
            print(userprofile.birthday)
            userprofile.alias = register_form.cleaned_data['alias']
            userprofile.save()
            user.userprofile = userprofile
            print("New user created.")
            return HttpResponseRedirect('/profile/')
    return HttpResponseRedirect('/login/')