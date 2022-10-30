from django.contrib import admin
from .models import Workshop, Level, WorkshopTestimonial


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    """Admin - display workshop level model fields"""
    list_display = ('level_name', 'friendly_name',)

    ordering = ('level_name',)


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    """Admin - display workshop model fields"""
    list_display = (
        'name',
        'level',
        'date',
        'start_time',
        'workshop_length',
        'workshop_fee',
        'location',
        'image'
        )

    list_filter = ('level', 'location')
    search_fields = ['name', 'description']

    ordering = ('name',)


@admin.register(WorkshopTestimonial)
class WorkshopTestimonialAdmin(admin.ModelAdmin):
    """Admin - display workshop testimonial model fields"""
    list_display = (
        'reviewer',
        'workshop',
        'date_added',
        'is_approved'
        )

    list_filter = ('reviewer', 'workshop')
    search_fields = ['reviewer', 'testimonial_body']

    ordering = ('workshop',)