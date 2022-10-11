"""Views for Product app"""

from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def show_all_products(request):
    """
    Show all products to the superuser,
    and only available ones to other users.
    """

    if request.user.is_superuser:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
    }
   
    return render(request, 'products/products.html', context)


def show_product_detail(request, product_id):
    """Show details of individual products."""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
