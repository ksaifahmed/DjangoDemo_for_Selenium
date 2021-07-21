from django.contrib import messages
from django.shortcuts import render, redirect

from login.models import CustomUser
from login.views import load_login
from register.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            phone = form.cleaned_data['phone']

            # check unique credentials

            user = CustomUser.objects.create_user(email, password, name, age, phone)
            user.save()
            messages.success(request, "Registration Successful! Please Login")
            return redirect(load_login)

    return render(request, 'register.html', {'form': form})
