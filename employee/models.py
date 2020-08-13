from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email
