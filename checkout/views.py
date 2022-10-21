"""Views for Checkout app"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """Show checkout page for the user to enter the detials and complete the order.
    Get basket from the session. If nothing in the basket, show error message and redirect back to product page.
    Create instance of Order Form (empty for now)."""
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, (
                "Your basket is empty at the moment. \
                Try adding something to purchase and try again!") 
            )
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)

    
