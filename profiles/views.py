"""Views for Profiles app"""
from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):
    """Display user profile page"""
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # populate form with user's current profile info
    form = UserProfileForm(instance=user_profile)
    # get user's orders
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
