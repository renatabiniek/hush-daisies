from django.contrib import admin
from .models import CustomRequest

# Register your models here.


@admin.register(CustomRequest)
class CustomRequestAdmin(admin.ModelAdmin):
    """Admin - display submitted queries"""
    list_display = (
        'name',
        'email',
        'request_type',
        'request_date',
        'request_body',
        )

    list_filter = ('name', 'request_body')

    ordering = ('request_date',)
