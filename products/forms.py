"""Product forms"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for superuser to add products to the store in the frontend
    """

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'is_available': 'Is the product ready for sale?'
        }

    # Replace image field on the form with widget field
    image = forms.ImageField(
        label="Image", required=False,
        widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        """
        Override init to make changes to the fields.
        Create list of tuples of the friendly names and category ids,
        to use as choices on the form
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-teal'
            self.fields['price'].widget.attrs['min'] = 0.01
