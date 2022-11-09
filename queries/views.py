"""Queries and Custom Requests View"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CustomRequestForm

# Create your views here.


def send_query(request):
    """
    View to show a query contact form.
    If POST: new instance of the product form.
    If form is valid, query gets submitted, with a message displayed.
    """

    if request.method == 'POST':
        form = CustomRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message was sent! '
                'We will get back to you within 48 hours.'
                )
            return redirect(reverse('send_query'))
        else:
            messages.error(
                request,
                'Message not sent. Please check the form \
                for errors and try submitting again.'
                )
    else:
        form = CustomRequestForm()

    template = 'queries/custom_request.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)
