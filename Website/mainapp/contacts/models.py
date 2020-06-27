from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.EmailField(max_length=180, default="", blank=True)
    phone = PhoneNumberField()
    message = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
