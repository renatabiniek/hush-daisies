"""View for workshops"""
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Level, Workshop

# Create your views here.


def show_workshops(request):
    """Show list of all workshops"""
    workshops = Workshop.objects.all()

    context = {
        'workshops': workshops,
    }

    return render(request, 'workshops/workshops.html', context)


def workshop_details(request, workshop_id):
    """Show details of individual workshops"""

    workshop = get_object_or_404(Workshop, pk=workshop_id)

    context = {
        'workshop': workshop,
    }

    return render(request, 'workshops/workshop_details.html', context)
