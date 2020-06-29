from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm (ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Please enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Please enter your email address'}),
            'phone': forms.TextInput(attrs={'placeholder':'Please enter your phone number'}),
            'message': forms.TextInput(attrs={'placeholder':'Please write me a message'})
        }