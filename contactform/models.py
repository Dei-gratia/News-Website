from __future__ import unicode_literals
from unicodedata import name
from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    txt = models.TextField()
    date = models.CharField(max_length=12, default="")
    time = models.CharField(max_length=12, default="")


    def __str__(self) :
        return self.name 
