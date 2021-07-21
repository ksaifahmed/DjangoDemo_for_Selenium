import re

from django import forms
from django.db import DatabaseError

from login.models import CustomUser
from register.validators import *


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ful Name",
                           widget=forms.TextInput(attrs={'class': 'name', 'id': 'name', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=100, label="Email",
                             widget=forms.TextInput(attrs={'class': 'email', 'id': 'email', 'placeholder': 'Email'}))
    age = forms.IntegerField(max_value=100, min_value=5, validators=[is_integer],
                             widget=forms.NumberInput(attrs={'class': 'age', 'id': 'age', 'placeholder': 'Age'}))
    phone = forms.IntegerField(max_value=8801999999999, min_value=8801100000000, validators=[is_integer],
                               widget=forms.NumberInput(
                                   attrs={'class': 'phone', 'id': 'phone', 'placeholder': 'Phone Number'})
                               )

    password = forms.CharField(widget=forms.PasswordInput(
                                attrs={'class': 'password',
                                       'id': 'password',
                                       'placeholder': 'Password'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(
                                        attrs={'class': 'c_password',
                                               'id': 'confirm_password',
                                               'placeholder': 'Confirm Password'}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password_ = cleaned_data.get("password")
        email = cleaned_data.get("email")
        confirm_password_ = cleaned_data.get("confirm_password")
        phone = cleaned_data.get("phone")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None
        except DatabaseError:
            user = None
        if user is not None:
            self.add_error('email', 'email already in use!')

        try:
            user = CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            user = None
        except DatabaseError:
            user = None
        if user is not None:
            self.add_error('phone', 'phone number already in use!')

        if not pass_strong(password_):
            string_msg = "password must be at least 8 characters that contain lowercase, uppercase, "
            string_msg += "numbers and special characters @?#!$%^&+="
            self.add_error('password', string_msg)

        if password_ != confirm_password_:
            self.add_error('confirm_password', "passwords do not match !")
        return cleaned_data


def pass_strong(password):
    return re.fullmatch(r'[A-Za-z0-9@?#!$%^&+=]{8,}', password)
