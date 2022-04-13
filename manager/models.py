from __future__ import unicode_literals
import email
from django.db import models

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=250)
    utxt = models.TextField()
    email = models.TextField(default="")


    def __str__(self) :
        return self.name 
