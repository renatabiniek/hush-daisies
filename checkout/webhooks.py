"""View for webhooks from Stripe"""
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWebhookHandler

import stripe

"""Credit: Code Institute, Boutique Ado walkthrough"""


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe,
    webhook view will be executed to handle the event
    """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    # generic exception handler
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = StripeWebhookHandler(request)

    # Event map dictionary
    # keys = Stripe webhooks names, values = methods inside the handler
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get webhook type from Stripe
    event_type = event['type']
    # Get handler from the event map dictionary
    event_handler = event_map.get(event_type, handler.handle_event)
    # Call event handler and pass in the event
    response = event_handler(event)
    return response
    