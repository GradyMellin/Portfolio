from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact


def createContact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("{% url 'home' %}")
    else:
        print(form.errors)
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contacts/contacts.html', context)