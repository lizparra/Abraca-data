# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20191128_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to=b''),
        ),
    ]
