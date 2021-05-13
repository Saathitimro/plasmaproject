from django.db import models
from datetime import datetime

# Create your models here.

class Donor(models.Model):
    Name = models.TextField(max_length=50)
    Contact = models.TextField(max_length=10)
    Address = models.TextField(max_length=100)
    Blood_type = models.TextField(max_length=10)
    Vacinated = models.BooleanField()
    Recovered = models.TextField(max_length=50)
    #this is to verify for the admin to call
    Verify = models.BooleanField(null=True,default=True)

class Blood(models.Model):
    Name = models.TextField(max_length=50)
    Contact = models.TextField(max_length=10)
    Blood_type = models.TextField(max_length=10)
