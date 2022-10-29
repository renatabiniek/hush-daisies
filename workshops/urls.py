"""URL paths for the Workshops app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_workshops, name='show_workshops'),
]
