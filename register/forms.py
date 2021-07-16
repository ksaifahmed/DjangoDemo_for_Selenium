from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ful Name",
                           widget=forms.TextInput(attrs={'class': 'name', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=100, label="Email",
                             widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Email'}))
    age = forms.IntegerField(max_value=100, min_value=5,
                             widget=forms.NumberInput(attrs={'class': 'age', 'placeholder': 'Age'}))
    phone = forms.IntegerField(max_value=8801999999999, min_value=8801100000000,
                               widget=forms.NumberInput(attrs={'class': 'phone', 'placeholder': 'Phone Number'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Password'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(
                                        attrs={'class': 'c_password', 'placeholder': 'Confirm Password'}))
