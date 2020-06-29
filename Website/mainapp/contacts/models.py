from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.EmailField(max_length=180, default="", blank=True)
    phone =  models.CharField(max_length=15, default="", blank=True)
    message = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
