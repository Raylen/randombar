from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist

from .models import Recipe, BoardGame, Event, FavouriteGame, FavouriteRecipe, AttendedEvent
from .forms import RecipeForm, BoardGameForm, EventForm


def menu_list(request):
    recipes = Recipe.objects.all().order_by('-volume', 'name')
    paginator = Paginator(recipes, 12)
    page = request.GET.get('page')
    try:
        tmp_entries = paginator.page(page)
    except PageNotAnInteger:
        tmp_entries = paginator.page(1)
    except EmptyPage:
        tmp_entries = paginator.page(paginator.num_pages)
    entries = [tmp_entries[x:x+3] for x in range(0, len(tmp_entries), 3)]
    num_pages = list(range(1, paginator.num_pages + 1))
    form = None
    if request.user.is_superuser:
        form = RecipeForm()
    return render(request, 'recipe_list.html', {'entries_list': tmp_entries,
                                                'rows': entries,
                                                'form': form,
                                                'pages': num_pages})


def games_list(request):
    games = BoardGame.objects.all().order_by('name')
    paginator = Paginator(games, 10)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    num_pages = list(range(1, paginator.num_pages + 1))
    form = None
    if request.user.is_superuser:
        form = BoardGameForm()
    return render(request, 'game_list.html', {'entries_list': entries, 'form': form, 'pages': num_pages})


def events_list(request):
    events = Event.objects.all().order_by('date_start')
    paginator = Paginator(events, 5)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    num_pages = list(range(1, paginator.num_pages + 1))
    form = None
    if request.user.is_superuser:
        form = EventForm()
    return render(request, 'event_list.html', {'entries_list': entries, 'form': form, 'pages': num_pages})


def menu_entry(request, item_id):
    item = get_object_or_404(Recipe, id=item_id)
    favourite = False
    if not request.user.is_anonymous:
        try:
            favourite = FavouriteRecipe.objects.get(user=request.user, recipe=item)
            favourite = True
        except ObjectDoesNotExist:
            pass
    return render(request, 'recipe_entry.html', {'entry': item, 'entry_id': item_id, 'favourite': favourite})


def games_entry(request, game_id):
    game = get_object_or_404(BoardGame, id=game_id)
    return render(request, 'game_entry.html', {'game': game, 'game_id': game_id})


def events_entry(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_entry.html', {'event': event, 'event_id': event_id})


@user_passes_test(lambda u: u.is_superuser)
def menu_entry_create(request, item_id=None):
    if request.method == 'GET':
        form = RecipeForm()
        part1 = list(form)[:3]
        part2 = list(form)[3:]
        context = {'form_part1': part1,
                   'form_part2': part2,
                   'form': form}
        return render(request, 'recipe_create.html', context)
    else:
        if item_id:
            entry = get_object_or_404(Recipe, id=item_id)
            form = RecipeForm(request.POST or None, request.FILES or None, instance=entry)
        else:
            form = RecipeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                recipes = Recipe.objects.all()
                html = loader.render_to_string('inc-admin_object_list.html', {'entries_list': recipes,
                                                                              'title': 'Список записей меню'},
                                               request=request)
                data = {'errors': False, 'html': html}
                return JsonResponse(data)
            return HttpResponseRedirect('/menu/')
        else:
            if request.is_ajax():
                errors = form.errors.as_json()
                return JsonResponse({'errors': errors})

        part1 = list(form)[:3]
        part2 = list(form)[3:]
        context = {'form_part1': part1,
                   'form_part2': part2,
                   'form': form}
        return render(request, 'recipe_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def games_entry_create(request, game_id=None):
    if request.method == 'GET':
        form = BoardGameForm()
        part1 = list(form)[:2]
        part2 = list(form)[2:]
        context = {'form_part1': part1,
                   'form_part2': part2}
        return render(request, 'game_create.html', context)
    else:
        if game_id:
            entry = get_object_or_404(BoardGame, id=game_id)
            form = BoardGameForm(request.POST or None, request.FILES or None, instance=entry)
        else:
            form = BoardGameForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                games = BoardGame.objects.all()
                html = loader.render_to_string('inc-admin_object_list.html', {'entries_list': games,
                                                                              'title': 'Список настольных игр'},
                                               request=request)
                data = {'errors': False, 'html': html}
                return JsonResponse(data)
            return HttpResponseRedirect('/games/')
        else:
            if request.is_ajax():
                errors = form.errors.as_json()
                return JsonResponse({'errors': errors})

        part1 = list(form)[:2]
        part2 = list(form)[2:]
        context = {'form_part1': part1,
                   'form_part2': part2}
        return render(request, 'game_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def events_entry_create(request, event_id=None):
    if request.method == 'GET':
        form = EventForm()
        part1 = list(form)[:2]
        part2 = list(form)[2:]
        context = {'form_part1': part1,
                   'form_part2': part2}
        return render(request, 'event_create.html', context)
    else:
        if event_id:
            entry = get_object_or_404(Event, id=event_id)
            form = EventForm(request.POST or None, request.FILES or None, instance=entry)
        else:
            form = EventForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                events = Event.objects.all()
                html = loader.render_to_string('inc-admin_object_list.html', {'entries_list': events,
                                                                              'title': 'Список событий'},
                                               request=request)
                data = {'errors': False, 'html': html}
                return JsonResponse(data)
            return HttpResponseRedirect('/events/')
        else:
            if request.is_ajax():
                errors = form.errors.as_json()
                return JsonResponse({'errors': errors})

        part1 = list(form)[:2]
        part2 = list(form)[2:]
        context = {'form_part1': part1,
                   'form_part2': part2}
        return render(request, 'event_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def menu_entry_delete(request, item_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=item_id)
        recipe.delete()
        if request.is_ajax():
            entries = Recipe.objects.all()
            html = loader.render_to_string('inc-admin_object_list.html', {'entries_list': entries,
                                                                          'title': 'Список объектов меню'},
                                           request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        return HttpResponseRedirect('/menu/')
    return HttpResponseRedirect('/menu/')


@user_passes_test(lambda u: u.is_superuser)
def games_entry_delete(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(BoardGame, id=game_id)
        game.delete()
        if request.is_ajax():
            entries = BoardGame.objects.all()
            html = loader.render_to_string('inc-admin_object_list.html', {'entries_list': entries,
                                                                          'title': 'Список настольных игр'},
                                           request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        return HttpResponseRedirect('/games/')
    return HttpResponseRedirect('/games/')


@user_passes_test(lambda u: u.is_superuser)
def events_entry_delete(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        if request.is_ajax():
            entries = Event.objects.all()
            html = loader.render_to_string('inc-admin_object_list.html', {'entries_list': entries,
                                                                          'title': 'Список событий'},
                                           request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        return HttpResponseRedirect('/events/')
    return HttpResponseRedirect('/events/')


def add_favourite_recipe(request, item_id):
    if request.method == 'POST':
        try:
            recipe = Recipe.objects.get(id=item_id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/menu/')
        try:
            entry = FavouriteRecipe.objects.get(user=request.user, recipe=recipe)
        except ObjectDoesNotExist:
            entry = None
        if entry:
            entry.delete()
        else:
            entry = FavouriteRecipe()
            entry.recipe = recipe
            entry.user = request.user
            entry.save()
        return HttpResponseRedirect('/menu/view/{0}'.format(item_id))
