"""SecondProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp.views import *
from admin_app.views import *
from content_app.views import *
from django.views.static import serve
from django.conf import settings

# mainapp views
urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^user/view/$', user_view, name='user_view'),
]

# admin views
urlpatterns += [
    url(r'^admin/$', admin, name='admin'),
    url(r'^admin/users_list/$', users_list, name='users_list'),
    url(r'^admin/get_user_form/(\d+)$', get_user_form, name='get_user_form'),
    url(r'^admin/user/create/(\d*)$', create_user, name='create_user'),
    url(r'^admin/user/delete/(\d+)$', delete_user, name='delete_user'),
    url(r'^user/register/$', registration, name='registration'),

    url(r'^admin/menu/list/$', admin_menu_list, name='admin_menu_list'),
    url(r'^admin/get_menu_form/(\d+)$', get_menu_form, name='get_menu_form'),

    url(r'^admin/games/list/$', admin_game_list, name='admin_games_list'),
    url(r'^admin/get_game_form/(\d+)$', get_game_form, name='get_game_form'),

    url(r'^admin/events/list/$', admin_events_list, name='admin_events_list'),
    url(r'^admin/get_event_form/(\d+)$', get_event_form, name='get_event_form'),
]

# content views
urlpatterns += [
    url(r'^menu/$', menu_list, name='menu_list'),
    url(r'^menu/view/(\d+)$', menu_entry, name='menu_entry'),
    url(r'^menu/create/(\d*)$', menu_entry_create, name='menu_create'),
    url(r'^menu/delete/(\d+)$', menu_entry_delete, name='menu_delete'),
    url(r'^menu/favourite/(\d+)$', add_favourite_recipe, name='add_favourite_recipe'),
    url(r'^games/$', games_list, name='games_list'),
    url(r'^games/view/(\d+)$', games_entry, name='games_entry'),
    url(r'^games/create/(\d*)$', games_entry_create, name='games_create'),
    url(r'^games/delete/(\d+)$', games_entry_delete, name='games_delete'),
    url(r'^events/$', events_list, name='events_list'),
    url(r'^events/view/(\d+)$', events_entry, name='events_entry'),
    url(r'^events/create/(\d*)$', events_entry_create, name='events_create'),
    url(r'^events/delete/(\d+)$', events_entry_delete, name='events_delete'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]