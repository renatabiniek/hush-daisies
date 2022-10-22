"""Views for Checkout app"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe

# Create your views here.


def checkout(request):
    """Show checkout page for the user to enter the detials and complete the order.
    Get basket from the session. If nothing in the basket, show error message and redirect back to product page.
    Create instance of Order Form (empty for now)."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, (
                "Your basket is empty at the moment. \
                Try adding something to purchase and try again!") 
            )
        return redirect(reverse('products'))
    # store the basket contents
    current_basket = basket_contents(request)
    # get the total
    total = current_basket['grand_total']
    # stripe requires the amount to charge as integer
    stripe_total = round(total * 100)
    # set the secret key on stripe and create payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    # message alert if no public key was set
    if not stripe_public_key:
        messages.warning(
            request,
            'Stripe public key is missing. \
            Did you forget to set it in your environment?'
            )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

    
