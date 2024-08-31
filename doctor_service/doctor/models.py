from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)