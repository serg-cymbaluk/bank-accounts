from django.shortcuts import render, redirect
from allauth.account.adapter import get_adapter


def index(request):
    return redirect('list-accounts')


def login(request):
    if request.user.is_authenticated():
        return redirect('index')
    return render(request, 'login.html')


def logout(request):
    get_adapter(request).logout(request)
    return redirect('login')
