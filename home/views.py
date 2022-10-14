"""Views for Home app"""

from django.shortcuts import render

# Create your views here.


def home(request):
    """Render a home page template"""
    return render(request, 'home/index.html')
