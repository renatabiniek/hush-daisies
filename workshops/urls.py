"""URL paths for the Workshops app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_workshops, name='show_workshops'),
    path('<int:workshop_id>/', views.workshop_details, name='workshop_details'),
    path('add/', views.add_workshop, name='add_workshop'),
]
