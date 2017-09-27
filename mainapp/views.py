from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        return HttpResponseRedirect("/")
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def main(request):
    return render(request, 'index.html', {'errors': False, 'title': 'Главная'})
