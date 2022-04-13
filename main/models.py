from __future__ import unicode_literals
from unicodedata import name
from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=250)
    about = models.TextField()
    abouttxt = models.TextField(default="")
    fb = models.CharField(max_length=50)
    tw = models.CharField(max_length=50)
    yt = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    set_name = models.CharField(max_length=50)

    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    def __str__(self) :
        return self.set_name + str(self.pk)
