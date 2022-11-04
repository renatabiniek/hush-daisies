"""Contact form for QUeries app"""

from django import forms
from .models import CustomRequest


class CustomRequestForm(forms.ModelForm):
    """
    Form to capture queries, qoutes
    and requests to save a spot for a workshop
    """
    class Meta:
        """Render all form fields"""
        model = CustomRequest
        exclude = ('request_date',)
        help_texts = {
            'reference_link': 'If you are looking for a custom order, '
            'add a link to a visual that will help us understand better '
            'what you have in mind',
            'request_body': 'Let us know why you are contacting us today.'
            'If you want to save your spot for a workshop,'
            'please specify the name of the workshop and the date',
            }
    field_order = ['request_type',
                   'name', 'email', 'phone_number',
                   'request_body', 'reference_link']

    def __init__(self, *args, **kwargs):
        """
        Override init method to
        set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-teal'
