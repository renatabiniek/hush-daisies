"""Views for Profiles app"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

# Create your views here.


def profile(request):
    """
    Display user profile page. If POST, create new instance of
    UserProfile form using the post data, updating the user_profile.
    Replace form variable with the update user profile
    and return the same template.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated.')

    # populate form with user's current profile info
    form = UserProfileForm(instance=user_profile)
    # get user's orders
    orders = user_profile.orders.all().order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        # used to hide basket contents in toast message on profile page
        'on_profile_page': True,
    }

    return render(request, template, context)


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

