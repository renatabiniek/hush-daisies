"""Views for Profiles app"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Workshop, WorkshopFavourites
from .forms import UserProfileForm

from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """
    Display user profile page. If POST, create new instance of
    UserProfile form using the post data, updating the user_profile.
    Replace form variable with the update user profile
    and return the same template.
    Display workshops on the favourite list in the user profile.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    favourites_list = None
    favourites = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated.')
        else:
            messages.error(
                request,
                'Profile not updated. Please check the form and try again.'
                )
    else:
        # populate form with user's current profile info
        form = UserProfileForm(instance=user_profile)

    # get user's orders
    orders = user_profile.orders.all().order_by('-date')
    # get favourites
    try:
        favourites_list = get_object_or_404(
            WorkshopFavourites,
            user=user_profile
            )
        favourites = favourites_list.workshop.all()
    except Http404:
        favourites_list = None

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favourites_list': favourites_list,
        'favourites': favourites,
        # used to hide basket contents in toast message on profile page
        'on_profile_page': True,
        'from_profile': True,
        }

    return render(request, template, context)


@login_required
def past_order(request, order_number):
    """Re-use the checkout_success template to display past order detail"""
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        # used to check if user got to checkout success via profile
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def workshop_favourites(request, workshop_id):
    """
    Add or remove favourite workshops.
    Get favourite list for the user, if exists.
    Create if it doesn't.
    """

    user_profile = get_object_or_404(UserProfile, user=request.user)
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    redirect_url = request.POST.get('redirect_url')

    try:
        favourites_list = get_object_or_404(
            WorkshopFavourites, user=user_profile
        )
    except Http404:
        favourites_list = WorkshopFavourites(user=user_profile)
        favourites_list.save()

    if workshop in favourites_list.workshop.all():
        favourites_list.workshop.remove(workshop)
        status = 'removed'
        favourites_list.save()

    else:
        favourites_list.workshop.add(workshop)
        status = 'added'
        favourites_list.save()

    messages.success(request, f'Workshop "{status}" to favourites')

    return redirect(redirect_url)
