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
        'stripe_public_key': 'pk_test_51LlW2kIf7v8zn8dZ59SVkupVfG4lyoY2Pb2pCnfPwC8OkYYdW5SFXcpiRnI652XFoGA2WIWuSsUxAvDYZNJ526Fz00y0Kg14rH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

    
