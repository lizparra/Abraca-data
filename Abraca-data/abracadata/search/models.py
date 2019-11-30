# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import django.utils.timezone as tz
# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=45, null=True)
    age = models.IntegerField(null=False)
    sex = models.IntegerField(null=False)
    spayed = models.BooleanField()
    color = models.CharField(max_length=45, null=True)
    fostered = models.BooleanField()
    acquired_date = models.DateField(null=False, default=tz.now())
    breed = models.CharField(max_length=50, null=False, default='Unknown')
    image = models.TextField(default='default.jpeg')
    slug = models.SlugField(default='unknown')
    description = models.TextField(default=' ')
    pet_id = models.CharField(max_length=8, null=False, default='No ID')

    def __str__(self):
        return self.name

    def get_sex(self):
        if self.sex == 1:
            return 'Female'
        elif self.sex == 0:
            return 'Male'
        else:
            return 'Unknown'

    def get_age(self):
        if self.age < 0:
            return 'Invalid age'

        years = self.age / 12
        months = self.age % 12

        if years == 1 and months == 1:
            return str(years) + ' year ' + str(months) + ' month'
        elif years == 1:
            return str(years) + ' year ' + str(months) + ' months'
        elif months == 1:
            return str(years) + ' years ' + str(months) + ' month'
        else:
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
