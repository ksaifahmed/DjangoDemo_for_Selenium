from django import forms
from register.validators import *


AREA_CHOICES = [
    ('Dhanmondi', 'Dhanmondi'),
    ('Uttara', 'Uttara'),
    ('Banani', 'Banani'),
    ('Mohammadpur', 'Mohammadpur'),
]


YES_NO_CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]

SERVICE_OPTIONS = [
    ('1', 'Refund on Return'),
    ('2', 'Exchange'),
    ('3', 'Free Delivery'),
    ('4', 'Free Servicing'),
]


class ProductForm(forms.Form):
    name = forms.CharField(max_length=250, min_length=1,
                           widget=forms.TextInput(
                               attrs={'class': 'input', 'id': 'p_name', 'placeholder': 'product name'})
                           )

    quantity = forms.IntegerField(min_value=1, validators=[is_integer],
                                  widget=forms.NumberInput(
                                      attrs={'class': 'input', 'id': 'quantity', 'placeholder': 'quantity'})
                                  )

    price = forms.FloatField(min_value=0.01,
                             widget=forms.NumberInput(
                                 attrs={'class': 'input', 'id': 'price', 'placeholder': 'price'})
                             )

    discount = forms.FloatField(min_value=0.0, max_value=100.0,
                                widget=forms.NumberInput(
                                    attrs={'class': 'input', 'id': 'discount', 'placeholder': 'discount %'})
                                )

    location = forms.ChoiceField(choices=AREA_CHOICES,
                                 widget=forms.Select(
                                     attrs={'class': 'input', 'id': 'location', 'placeholder': 'location'})
                                 )

    warranty = forms.ChoiceField(choices=YES_NO_CHOICES, label='warranty',
                                 widget=forms.RadioSelect(
                                     attrs={'class': 'radio_input', 'id': 'warranty'})
                                 )
    additional_options = forms.MultipleChoiceField(
        choices=SERVICE_OPTIONS, label='warranty',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'radio_input', 'id': 'additional_options'})
    )
