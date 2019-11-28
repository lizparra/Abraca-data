# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    sex = models.IntegerField()
    spayed = models.BooleanField()
    size = models.CharField(max_length=15)
    color = models.CharField(max_length=45)
    fostered = models.BooleanField()
    acquired_date = models.DateField(auto_now_add=True)
    breed_id_fk = models.IntegerField()
    image = models.CharField(max_length=250)


def __str__(self):
    return self.name