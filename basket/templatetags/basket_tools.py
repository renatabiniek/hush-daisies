"""
Custom template filter to 
calculate subtotal for basket.html
"""
from django import template

register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subotal(price, quantity):
    """Calculate total of quantity times item price"""
    return price * quantity
