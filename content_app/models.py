from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Название', max_length=100)
    # Вид рецепта - True = напиток, False = еда
    recipe_type = models.BooleanField(verbose_name='Вид рецепта')
    description = models.CharField(verbose_name='Описание', max_length=500, blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='img/', blank=True, null=True)
    volume = models.IntegerField(verbose_name='В наличии', blank=True, null=True)
    price = models.FloatField(verbose_name='Цена')
    ingredients = models.CharField(verbose_name='Состав', max_length=500, blank=True, null=True)


class BoardGame(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=500, blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='img/', blank=True, null=True)
    availability = models.BooleanField(verbose_name='Наличие')


class Event(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=500, blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='img/', blank=True, null=True)
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    price = models.FloatField(verbose_name='Плата за участие', blank=True, null=True)
    game = models.ForeignKey(BoardGame, verbose_name='Игра', blank=True, null=True)


class FavouriteGame(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    game = models.ForeignKey(BoardGame, verbose_name='Игра')


class FavouriteRecipe(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, verbose_name='Еда')


class AttendedEvent(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    event = models.ForeignKey(Event, verbose_name='Событие')
