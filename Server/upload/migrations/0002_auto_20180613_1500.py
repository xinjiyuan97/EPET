# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-13 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadphotos',
            name='experimentId',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uploadphotos',
            name='resourcesId',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='uploadphotos',
            name='filePath',
            field=models.ImageField(upload_to=upload.models.lessonsPath),
        ),
    ]