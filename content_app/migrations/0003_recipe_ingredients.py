# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0002_auto_20170913_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(blank=True, max_length=500, verbose_name='Состав'),
        ),
    ]