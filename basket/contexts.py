"""Context processor for basket content"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):
    """
    Context processor that returns context dictionary
    and makes it available to all templates 
    in the whole application.
    """

    basket_items = []
    total = 0
    product_count = 0
    # get the basket from the session
    basket = request.session.get('basket', {})
    # iterate through items in the basket from the session
    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_countdown = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_countdown = 0
    
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_countdown': free_delivery_countdown,
        'free_delivery_treshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context