from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    roll = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
