"""URL paths for the Queries app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_query, name='send_query'),
]