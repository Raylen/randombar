from django import forms
from .models import Recipe, Event, BoardGame


class RecipeForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Название', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Название'}))
    description = forms.CharField(required=False, label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Описание'}))
    photo = forms.ImageField(required=False, label='Фото', widget=forms.FileInput())
    recipe_type = forms.BooleanField(required=False, label='Напиток?', widget=forms.CheckboxInput())
    volume = forms.IntegerField(required=False, label='В наличии',
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'placeholder': '0.00'}))
    price = forms.FloatField(required=True, label='Цена',
                             widget=forms.NumberInput(attrs={'class': 'form-control',
                                                             'placeholder': '0.00'}))
    ingredients = forms.CharField(required=False, label='Состав',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Состав'}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'photo', 'volume', 'price', 'recipe_type', 'ingredients']


class BoardGameForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Название', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Название'}))
    description = forms.CharField(required=False, label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Описание'}))
    photo = forms.ImageField(required=False, label='Фото', widget=forms.ClearableFileInput())
    availability = forms.BooleanField(required=False, label='Наличие', widget=forms.CheckboxInput())

    class Meta:
        model = BoardGame
        fields = ['name', 'description', 'photo', 'availability']


class EventForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Название', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Название'}))
    description = forms.CharField(required=False, label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Описание'}))
    photo = forms.ImageField(required=False, label='Фото', widget=forms.ClearableFileInput())
    date_start = forms.DateField(required=True, label='Дата начала',
                                 widget=forms.DateInput(attrs={'class': 'form-control'}))

    date_end = forms.DateField(required=True, label='Дата окончания',
                               widget=forms.DateInput(attrs={'class': 'form-control'}))

    price = forms.FloatField(required=False, label='Плата за участие',
                             widget=forms.NumberInput(attrs={'class': 'form-control',
                                                             'placeholder': '0.00'}))

    game_qs = BoardGame.objects.all()
    game = forms.ModelChoiceField(queryset=game_qs, required=False, label='Игра',
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ['name', 'description', 'photo', 'date_start', 'date_end', 'price', 'game']
