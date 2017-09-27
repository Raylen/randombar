# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0005_auto_20170913_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content_app.BoardGame', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Плата за участие'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='volume',
            field=models.IntegerField(blank=True, null=True, verbose_name='В наличии'),
        ),
    ]