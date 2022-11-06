"""Views for Checkout app"""
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from basket.contexts import basket_contents

import stripe
import json

# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
    Make POST request with client secret from the payment
    intent before calling confirmed payment method in stripe js.
    Split to get the payment intent id. Set up Stripe with
    the secret key to modify the payment intent.
    Return status=200 for OK, status=400 for error.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, 'Sorry, your payment cannot be processed right now. \
                      Please try again later.'
                      )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """Show checkout page for the user to enter the detials
    and complete the order. Get basket from the session.
    If nothing in the basket, show error message and redirect back
    to product page. Create instance of Order Form (empty for now).
    If POST request: get basket, put form data into dictionary,
    create instance of the form. If form is valid, save the order.
    """
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
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
                        request, "One of the products in your basket couldn't \
                        be found in our database. Please contact us for help."
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

        if request.user.is_authenticated:
            # generate pre-populated order form
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': str(profile.user),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'house_number_or_name':
                    profile.default_house_number_or_name,
                    'street_address_1': profile.default_street_address_1,
                    'street_address_2': profile.default_street_address_2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            # empty form if user not authenticated
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
    Show order completion confirmation page with order summary.
    If user logged in, assign order to user.
    If save info box was checked, pull data from order to user profile.
    Create instance of UserProfileForm using the form data.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attached the user profile to the order
        order.user_profile = profile
        order.save()
        # Save user information
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_house_number_or_name': order.house_number_or_name,
                'default_street_address_1': order.street_address_1,
                'default_street_address_2': order.street_address_2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
    messages.success(
        request,
        f'Your order was received. '
        f'Order confirmation will be sent to { order.email }.')
    # delete basket from the session
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
