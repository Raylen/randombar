from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Логин'}))
    email = forms.EmailField(required=True, label='E-Mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Адрес почты'}))
    password1 = forms.CharField(required=True, label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Повторите пароль'}))
    first_name = forms.CharField(required=False, label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Имя пользователя'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')


class UserChangeForm(forms.ModelForm):

    """
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    """
    username = forms.CharField(required=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Логин'}))
    email = forms.EmailField(required=True, label='E-Mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Адрес почты'}))
    first_name = forms.CharField(required=False, label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Имя пользователя'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']