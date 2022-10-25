"""URL paths for the Profiles app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('past_order/<order_number>', views.past_order, name='past_order'),
]
