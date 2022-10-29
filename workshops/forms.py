"""Workshop forms"""
from django import forms
from products.widgets import CustomClearableFileInput
from .models import Workshop, Level


class WorkshopForm(forms.ModelForm):
    """
    Form for superuser to add workshops in the frontend
    """

    class Meta:
        model = Workshop
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
                ),
            'start_time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'type': 'time'}
                ),
            }

    def __init__(self, *args, **kwargs):
        """
        Override init to make changes to the fields.
        Create list of tuples of the friendly names and level ids,
        to use as choices on the form
        """
        super().__init__(*args, **kwargs)
        levels = Level.objects.all()
        friendly_names = [(lev.id, lev.get_friendly_name()) for lev in levels]

        self.fields['level'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-teal'
