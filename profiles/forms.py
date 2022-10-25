"""User profile form for Profiles app"""

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Form to capture default user info"""
    class Meta:
        """
        Render all form fields except 'user'
        as this shouldn remain the same
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Override init method to add placeholders and class,
        and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_house_number_or_name': 'House Number or Name',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, Region or State',
            'default_postcode': 'Post code or Eircode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
