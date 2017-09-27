from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf

from .forms import UserRegistrationForm, UserChangeForm
from content_app.models import Recipe, BoardGame, Event, FavouriteRecipe, FavouriteGame, AttendedEvent
from content_app.forms import RecipeForm, BoardGameForm, EventForm


@user_passes_test(lambda u: u.is_superuser)
def admin(request):
    return render(request, "admin_page.html")


@user_passes_test(lambda u: u.is_superuser)
def users_list(request):
    users = User.objects.all()
    form = UserRegistrationForm()
    return render(request, 'admin_users_list.html', {'users_list': users, 'form': form})


def get_user_form(request, user_id):
    """
    Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
    """
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = UserRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': UserRegistrationForm()}
    return render(request, 'registration.html', context)


def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан user_id
    """
    if request.is_ajax():
        if not user_id:
            user = UserChangeForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users_list': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    users = User.objects.all()
    html = loader.render_to_string('inc-users_list.html', {'users_list': users}, request=request)
    data = {'errors': False, 'html': html}
    return JsonResponse(data)


@user_passes_test(lambda u: u.is_superuser)
def admin_menu_list(request):
    menu = Recipe.objects.all()
    form = RecipeForm()
    return render(request, 'admin_menu_list.html', {'entries_list': menu,
                                                    'form': form,
                                                    'title': 'Список записей меню'})


def get_menu_form(request, item_id):
    if request.is_ajax():
        entry = get_object_or_404(Recipe, id=item_id)
        form = RecipeForm(instance=entry)
        context = {'form': form,
                   'id': item_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-admin_object_create_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


@user_passes_test(lambda u: u.is_superuser)
def admin_game_list(request):
    games = BoardGame.objects.all()
    form = BoardGameForm()
    return render(request, 'admin_game_list.html', {'entries_list': games,
                                                    'form': form,
                                                    'title': 'Список настольных игр'})


def get_game_form(request, item_id):
    if request.is_ajax():
        entry = get_object_or_404(BoardGame, id=item_id)
        form = BoardGameForm(instance=entry)
        context = {'form': form,
                   'id': item_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-admin_object_create_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


@user_passes_test(lambda u: u.is_superuser)
def admin_events_list(request):
    events = Event.objects.all()
    form = EventForm()
    return render(request, 'admin_events_list.html', {'entries_list': events,
                                                      'form': form,
                                                      'title': 'Список событий'})


def get_event_form(request, item_id):
    if request.is_ajax():
        entry = get_object_or_404(Event, id=item_id)
        form = EventForm(instance=entry)
        context = {'form': form,
                   'id': item_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-admin_object_create_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


@user_passes_test(lambda u: not u.is_anonymous)
def user_view(request):
    favourite_menu = FavouriteRecipe.objects.filter(user=request.user).select_related('recipe')
    favourite_drinks = [x.recipe for x in favourite_menu.filter(recipe__recipe_type=True)]
    favourite_meals = [x.recipe for x in favourite_menu.filter(recipe__recipe_type=False)]
    favourite_games = FavouriteGame.objects.filter(user=request.user).select_related('game')
    events = AttendedEvent.objects.filter(user=request.user).select_related('event')
    return render(request, 'user_view.html', {'favourite_drinks': favourite_drinks,
                                              'favourite_meals': favourite_meals,
                                              'favourite_games': favourite_games,
                                              'events': events})
