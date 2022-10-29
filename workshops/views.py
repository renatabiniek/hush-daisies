"""View for workshops"""
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Level, Workshop

# Create your views here.


def show_workshops(request):
    """Show list of all workshops"""
    workshops = Workshop.objects.all()
    # Sorting
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            # Create the sortkey variable
            sortkey = request.GET['sort']
            sort = sortkey
            # Allow case insensitive sorting by workshop name by adding temporary field on the Workshop model
            if sortkey == "name":
                sortkey = 'lower_name'
                workshops = workshops.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Reverse the sorting order if direction descending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # Use model method to sort workshops
            workshops = workshops.order_by(sortkey)

    # Return the sorting methodology to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'workshops': workshops,
        'current_sorting': current_sorting,
    }

    return render(request, 'workshops/workshops.html', context)


def workshop_details(request, workshop_id):
    """Show details of individual workshops"""

    workshop = get_object_or_404(Workshop, pk=workshop_id)

    context = {
        'workshop': workshop,
    }

    return render(request, 'workshops/workshop_details.html', context)
