"""URL paths for the Workshops app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_workshops, name='show_workshops'),
    path(
        '<int:workshop_id>/',
        views.workshop_details,
        name='workshop_details'
        ),
    path('add/', views.add_workshop, name='add_workshop'),
    path('edit/<int:workshop_id>/', views.edit_workshop, name='edit_workshop'),
    path(
        'delete/<int:workshop_id>/',
        views.delete_workshop,
        name='delete_workshop'
        ),
    path(
        'edit_testimonial/<int:testimonial_id>/',
        views.edit_testimonial,
        name='edit_testimonial'
        ),
    path(
        'delete_testimonial/<int:testimonial_id>/',
        views.delete_testimonial,
        name='delete_testimonial'),
]
