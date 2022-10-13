"""Views for Product app"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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

    cats = Category.objects.all()
    categories = None
    search_term = None
    sort = None
    direction = None

    if request.GET:
        # Filter by category
        if 'category' in request.GET:
            # split it into a list at the commas
            categories = request.GET['category'].split(',')
            # use the list to filter the current query set
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        # Search
        if 'q' in request.GET:
            search_term = request.GET['q']
            # if the query is blank
            if not search_term:
                messages.error(
                    request, "You didn't enter anything in the search field.")
                return redirect(reverse('products'))
            # if the query is not blank; returning results where the search term matched in either product name or description with case insensitive queries
            matched_terms = Q(name__icontains=search_term) | Q(
                description__icontains=search_term)
            products = products.filter(matched_terms)
        # Sorting
        if 'sort' in request.GET:
            # Create the sortkey variable
            sortkey = request.GET['sort']
            sort = sortkey
            # Allow case insensitive sorting by product name by adding temporary field on the Product model
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Reverse the sorting order if direction descending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # Use model method to sort products
            products = products.order_by(sortkey)

    # Return the sorting methodology to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_categories': categories,
        'cats': cats,
        'search_term': search_term,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def show_product_detail(request, product_id):
    """Show details of individual products."""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
