from django.contrib.auth import logout
from django.shortcuts import render, redirect


def load_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "home.html")


def user_logout(request):
    logout(request)
    return redirect('login')
