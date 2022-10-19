"""Views for Basket app"""
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_basket(request):
    """Show items in the basket"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add item to the basket.
    Get the quantity from the form, convert to integer.
    Use session to store information - check if basket variable in the session, if not, create empty dictionary.
    If matching item (item key) already in the bag, increase qty. Otherwise, add it to the basket.
    Put basket variable into the session, which overrides the variable in the session with the updated version.
    Redirect the user to the redirect_url.
    Get the product and add messages.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Quantity of {product.name.title()} updated to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{product.name.title()} added to the basket')
    
    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust basket content.
    Redirect always to the shopping basket page.
    If qty > 0, set new qty, otherwise remove item.
    Override session with new basket content.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    print(quantity)

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Quantity of {product.name.title()} updated to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'{product.name.title()} removed from the basket')
          
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove item from the basket. Intended qty is zero.
    Get basket from the session, remove item, override the basket session.
    Http 200 repsonse implying that the item was removed.
    If error, raisew server error (http 500)
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'{product.name.title()} removed from the basket')
        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=500) 
