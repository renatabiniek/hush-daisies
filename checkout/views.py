"""Views for Checkout app"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from basket.contexts import basket_contents

import stripe

# Create your views here.


def checkout(request):
    """Show checkout page for the user to enter the detials and complete the order.
    Get basket from the session. If nothing in the basket, show error message and redirect back to product page.
    Create instance of Order Form (empty for now).
    If POST request: get basket, put form data into dictionary, create instance of the form.
    If form is valid, save the order. """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        # form data done manually to skip the save info box
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'house_number_or_name ': request.POST['house_number_or_name'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        # create instance of the form
        order_form = OrderForm(form_data)
        # if form is valid save the order
        if order_form.is_valid():
            order = order_form.save()
            # iterate through the basket contents to create line items
            for item_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request, "One of the products in your basket couldn't be found \
                        in our database. Please contact us for help."
                        )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number])
                )
        else:
            messages.error(
                request, 'There was an error with the information you entered \
                          in the form. Please review your details \
                          and try again.'
                          )
    else:
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


def checkout_success(request, order_number):
    """
    Show order completion confirmation page with order summary 
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request, f'Your order { order_number } has been \
                   successfully processed. Order confirmation \
                   will be sent to { order.email }.'
                   )
    # delete basket from the session
    if 'basket' in request.session:
        del request.session['basket']
    
    template = 'checkout/checkout_succes.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
