"""Views for Basket app"""
from django.shortcuts import render, redirect

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
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    
    request.session['basket'] = basket
    return redirect(redirect_url)
