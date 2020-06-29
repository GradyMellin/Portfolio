from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact


def createContact(request):
    if request.is_ajax and request.method=="POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)