"""Admin setup for orders and checkout"""
from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Shows list of editable line items within the order.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Admin setup for Order model """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid',
    )

    fields = (
        'order_number',
        'user_profile',
        'date',
        'full_name',
        'email',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'town_or_city',
        'county',
        'postcode',
        'country',
        'order_total',
        'delivery_cost',
        'grand_total',
        'original_basket',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
