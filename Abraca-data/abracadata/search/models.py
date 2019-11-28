# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=45, null=True)
    age = models.IntegerField(null=False)
    sex = models.IntegerField(null=False)
    spayed = models.BooleanField()
    size = models.CharField(max_length=15, null=True)
    color = models.CharField(max_length=45, null=True)
    fostered = models.BooleanField()
    acquired_date = models.DateField(auto_now_add=True, null=False)
    breed = models.CharField(max_length=50, null=False, default='Unknown')
    image = models.ImageField(default='default.jpeg', blank=True)
    slug = models.SlugField(default='unknown')

    def __str__(self):
        return self.name

    def get_sex(self):
        if self.sex == 1:
            return 'Female'
        elif self.sex == 0:
            return 'Male'
        else:
            return 'ERROR'

    def get_age(self):
        if self.age < 0:
            return 'Invalid age'

        years = self.age / 12
        months = self.age % 12

        return str(years) + ' years ' + str(months) + ' months'

    def get_spayed(self):
        if self.spayed:
            return 'yes'
        else:
            return 'no'

    def get_fostered(self):
            if self.fostered:
                return 'yes'
            else:
                return 'no'
