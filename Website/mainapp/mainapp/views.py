from django.http import HttpResponse
from django.shortcuts import render
from contacts.forms import ContactForm


def home(request):
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, "home.html", context)


