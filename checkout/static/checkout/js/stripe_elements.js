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
 var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
 var client_secret = $('#id_client_secret').text().slice(1, -1);
// Create instance of stripe elements using public key
var stripe = Stripe(stripe_public_key);
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

