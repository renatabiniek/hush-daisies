from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin - display category model fields"""
    list_display = ('friendly_name', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin - display product model fields"""
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'is_available',
        'image'
        )
    list_filter = ('category', 'is_available')
    search_fields = ['name', 'description']

    ordering = ('name',)