"""Views for Profiles app"""
from django.shortcuts import render

# Create your views here.


def profile(request):
    """Display user profile page"""
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
