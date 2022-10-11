"""Views for Product app"""

from django.shortcuts import render, get_object_or_404
from .models import Product, Category

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

    categories = None
    cats = Category.objects.all()

    if request.GET:
        # Filter by category
        if 'category' in request.GET:
            # split it into a list at the commas
            categories = request.GET['category'].split(',')
            # use the list to filter the current query set
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
        'cats': cats,
    }

    return render(request, 'products/products.html', context)

def show_product_detail(request, product_id):
    """Show details of individual products."""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
