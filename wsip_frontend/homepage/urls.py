from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_steam_games', views.get_steam_games, name='get_steam_games')
]