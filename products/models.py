from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        """Correct the spelling for the plural form"""
        verbose_name_plural = 'Categories'

    """Category model"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """Return the category name"""
        return self.name

    def get_friendly_name(self):
        """Return the user friendly name"""
        return self.friendly_name


class Product(models.Model):
    """Products model"""
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products'
        )
    sku = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        editable=False
        )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """Return the product name"""
        return self.name
