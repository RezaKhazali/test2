from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

__author__ = 'saeed'


def index(request):
    return render(request, 'index.html')
