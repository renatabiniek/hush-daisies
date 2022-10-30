"""View for workshops"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Level, Workshop
from .forms import WorkshopForm

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
    workshop_testimonials = workshop.workshop_testimonials.filter(
        is_approved=True).order_by('-date_added')

    context = {
        'workshop': workshop,
        'workshop_testimonials': workshop_testimonials,
    }

    return render(request, 'workshops/workshop_details.html', context)


@login_required
def add_workshop(request):
    """
    View for superuser to add workshop in the frontend.
    If POST: new instance of the workshop form.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do that!')
        return redirect(reverse('show_workshops'))

    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            workshop = form.save()
            messages.success(
                request, f'New workshop "{ workshop }" was added!'
                )
            return redirect(reverse('workshop_details', args=[workshop.id]))
        else:
            messages.error(
                request,
                'Workshop not added. Please check the form \
                for errors and try submitting again.'
                )
    else:
        form = WorkshopForm()

    template = 'workshops/add_workshop.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def edit_workshop(request, workshop_id):
    """
    View for superuser to edit workshop details in the frontend.
    If POST: new instance of the workshop form matched with workshop id
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do that!')
        return redirect(reverse('show_workshops'))

    workshop = get_object_or_404(Workshop, pk=workshop_id)
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Workshop "{ workshop }" was updated!'
                )
            return redirect(reverse('workshop_details', args=[workshop.id]))
        else:
            messages.error(
                request,
                'Workshop not updated. Please check the form \
                for errors and try submitting again.'
                )
    else:
        form = WorkshopForm(instance=workshop)
        messages.info(request, f'You are editing "{workshop}"')

    template = 'workshops/edit_workshop.html'
    context = {
        'form': form,
        'workshop': workshop,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def delete_workshop(request, workshop_id):
    """View for admin to delete a workshop"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do that!')
        return redirect(reverse('show_workshops'))

    workshop = get_object_or_404(Workshop, pk=workshop_id)
    workshop.delete()
    messages.success(request, f'Workshop "{workshop}" deleted!')
    return redirect(reverse('show_workshops'))