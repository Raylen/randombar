# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
    ]
