"""Views for Basket app"""
from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """Show items in the basket"""
    return render(request, 'basket/basket.html')
