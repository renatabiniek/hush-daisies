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
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook from Stripe, sent each time user completes payment process.
        Use payment intent to create an order in case the checkout form isn't submitted.
        Check if order exists in the databes, return confirmation response
        if it does, and create order - if doesn't exist yet.
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        # replace empty strings in non-required fields with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        # check if order exists
        order_exists = False
        try:
            order = Order.object.get(
                full_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.address.country,
                postcode__iexact=shipping_details.address.postal_code,
                town_or_city__iexact=shipping_details.address.city,
                street_address_1__iexact=shipping_details.address.line1,
                street_address_2__iexact=shipping_details.address.line2,
                county__iexact=shipping_details.address.state,
                grand_total=grand_total,
                )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | '
                        'SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                # create order
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    )
                # load basket from json version in the payment intent and iterate
                for item_id, quantity in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as error:
                # delete order if any errors
                if order:
                    order.delete()
                # return error 500 so that Stripe can try again later
                return HttpResponse(content=f'Webhook received: {event["type"]} | '
                                            f'ERROR: {error}', status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.failed webhook from Stripe, if payment fails.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
