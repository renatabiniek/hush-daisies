from django.http import HttpResponse

"""Handler for Stripe webhooks"""
"""Credit: Code Institute, Boutique Ado walkthrough"""


class StripeWebhookHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """
        Setup method call when instance 
        of the class is created.
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unkonwn/unexpected webhook event.
        Take the event sent from Stripe, return HTTP response
        indicating it was received
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )
