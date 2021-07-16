from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label="Email",
                             widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))
