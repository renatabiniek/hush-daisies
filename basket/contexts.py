"""Context processor for basket content"""
from decimal import Decimal
from django.conf import settings

def basket_contents(request):
    """
    Context processor that returns context dictionary
    and makes it available to all templates 
    in the whole application.
    """

    basket_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
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