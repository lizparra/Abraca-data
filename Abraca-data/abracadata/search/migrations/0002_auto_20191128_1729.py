# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='breed_id_fk',
        ),
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
