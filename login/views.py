from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import CustomUser
from django.db import DatabaseError


def load_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email_ = form.cleaned_data['email']
            password_ = form.cleaned_data['password']

            # getting user
            try:
                user = CustomUser.objects.get(email=email_)
            except CustomUser.DoesNotExist:
                user = None
            except DatabaseError:
                return redirect("error")

            if user is not None:
                if user.check_password(password_):
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html',
                                  {'form': form, 'failed_login': 'incorrect password'})
            else:
                return render(request, 'login.html', {'form': form, 'failed_login': 'incorrect username'})

    return render(request, 'login.html', {'form': form})

