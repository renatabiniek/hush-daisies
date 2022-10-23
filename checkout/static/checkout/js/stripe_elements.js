/**
 * Handles creating Stripe elements and submitting payment form 
 * Credit: Code Institute, Boutique Ado walkthrough
 */

/*
 Core logic/payment flow comes from:
 https://stripe.com/docs/payments/accept-a-payment

 CSS from here: https://stripe.com/docs/stripe-js
 */

 // Get Stripe public key and client secret
 var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
 var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Create instance of stripe elements using public key
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Create card element, add style and mount it to the Payment details in checkout.html
var style = {
  base: {
      color: '#2B5357',
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '16px',
      letterSpacing: '2px',
      fontSmoothing: 'antialiased',
      '::placeholder': {
        color: '#aab7c4',
      },
    },
    invalid: {
      iconColor: '#dc3545',
      color: '#dc3545',
    },
  };

var card = elements.create('card', {style: style});
card.mount('#card-element',);

// Handle real-time validation for errors on the card element
card.addEventListener('change', function(event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
      <span role="alert">
          <i class="bi bi-x-square-fill" aria-hidden="true"></i>
      </span>
      <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
})

// Handle form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {
    // prevent default submission
    event.preventDefault();
    // disable to prevent multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // fade out payment form and trigger spinner
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    // get boolean value of save info box
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // get value of csrf token from using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // object to pass this to cache_checkout_data view
    var postData = {
      'csrfmiddlewaretoken': csrfToken,
      'client_secret': clientSecret,
      'save_info': saveInfo,
    };
    // triggers cache_checkout_data view
    var url = '/checkout/cache_checkout_data/';
    // post to the cache_checkout_data view and wait for the response
    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        house: $.trim(form.house_number_or_name.value),
                        line1: $.trim(form.street_address_1.value),
                        line2: $.trim(form.street_address_2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    house: $.trim(form.house_number_or_name.value),
                    line1: $.trim(form.street_address_1.value),
                    line2: $.trim(form.street_address_2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span role="alert">
                        <i class="bi bi-x-square-fill" aria-hidden="true"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                // re-enable
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
      }).fail(function() {
        // if status=400 returned, reload page
        location.reload();
      });
});