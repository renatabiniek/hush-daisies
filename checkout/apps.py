"""Config for Checkout app"""

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ Override the ready method, import signals """
        import checkout.signals
