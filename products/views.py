from django.shortcuts import render
from .models import Product

# Create your views here.


def show_all_products(request):
    """Show all available products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
