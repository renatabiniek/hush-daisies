"""URL paths for the Home app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
