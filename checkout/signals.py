"""
Singals are sent by Django once OrderLineItem model instance
is saved or deleted. Django built-in feature to execute
update_total method from models each time a line is attached to the order.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Handles signals from the post_save event.
    Update order total once line item is created/updated.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Handles signals from the post_delete event.
    Update order total once line item is deleted.
    """
    instance.order.update_total()
