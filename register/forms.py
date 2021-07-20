from django import forms
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
        attrs={'class': 'password', 'id': 'password', 'placeholder': 'Password'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(
                                        attrs={'class': 'c_password',
                                               'id': 'confirm_password',
                                               'placeholder': 'Confirm Password'}))
