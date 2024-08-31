from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    clinic_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.name
