"""
Checkout App Views
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from bag.contexts import bag_contents
from .forms import OrderForm


# Create your views here.
def checkout(request):
    """
    Checkout View
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse, ('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)
    
    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KqNjBJNHe4SfQuD0meT8GKqlXjnW7qwhhhIodFgHlm7AkxKeV2MYPRCL69OFrioiO3tbAG9vNQgku8RJksM5af000EM7cD2KD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
