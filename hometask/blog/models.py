from ast import Name
from unicodedata import name
from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField( max_length= 100)
    address = models.CharField( max_length= 100)
    phone = models.CharField( max_length= 100)

