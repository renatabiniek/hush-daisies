"""Order form for checkout app"""

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """Form to capture customer info and delivery details"""
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'house_number_or_name',
            'street_address_1',
            'street_address_2',
            'town_or_city',
            'county',
            'postcode',
            'country',
        )
    
    def __init__(self, *args, **kwargs):
        """
        Override init method to add placeholders and class, 
        and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Your Full Name',
            'email': 'youremail@example.com',
            'phone_number': 'Phone Number',
            'house_number_or_name': 'House no or name',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, Region or State',
            'postcode': 'Post code or Eircode',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

