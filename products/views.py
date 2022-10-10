from django.shortcuts import render
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
