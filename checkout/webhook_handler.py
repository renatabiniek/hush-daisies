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
            content=f'Unhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook from Stripe, sent each time user completes payment process.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.failed webhook from Stripe, if payment fails.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )
