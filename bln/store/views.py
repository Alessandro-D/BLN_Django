from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from bln.settings import PAYPAL_RECEIVER_EMAIL, HOST
import random

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Retrieve user's Byond key from the url
    bkey = request.GET.get('bkey')
    
    # What you want the Paypal button to do.
    paypal_dict = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "amount": "7.00",
        "item_name": "Subscription",
        "invoice": str(random.randint(0,999999)),
        "currency_code" : "USD",
        "notify_url": 'http://{}{}'.format(HOST, reverse('paypal-ipn')),
        "return": 'http://{}{}'.format(HOST, reverse('index')),
        "cancel_return": 'http://{}{}'.format(HOST, reverse('index')),
        "custom": bkey,  # Custom command to correlate to some function later (optional)
    }

    ppurl = 'http://{}{}'.format(HOST, reverse('paypal-ipn'))

    dict1 = dict(paypal_dict)
    dict2 = dict(paypal_dict)

    # Create the instances.
    btn5c = PayPalPaymentsForm(initial=dict1)

    dict2["amount"] = "10.00"
    btn10c = PayPalPaymentsForm(initial=dict2)

    # Render the HTML template index.html with the data in the context variable
    context={
        "btn5c" : btn5c,
        "btn10c" : btn10c,
        "bkey" : bkey,
        # "ppurl" : ppurl,
    }
    return render(request, 'index.html', context=context)