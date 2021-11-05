from django.shortcuts import render
from django.http import HttpResponse

from .forms import SteamIdForm
from random import randint
import requests
# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')


def get_steam_games(request):
    print(request.method)
    if request.method == 'POST':

        api_request = requests.get('http://localhost:3000/api/{}'.format(request.POST['steamIdInput']))
        

        if api_request.status_code == 200:
            
            response = api_request

            listOfSteamGames = response.json()
            randomGame = select_random_game(response.json())
            gameImageUrl = 'http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg'.format(randomGame['appid'], randomGame['img_logo_url'])

            return render(request, 'homepage/result.html', {
                'listOfSteamGames': listOfSteamGames,
                'randomGame': randomGame,
                'gameImageUrl': gameImageUrl
                }) 
            # return HttpResponse(api_request.json())

        if api_request.status_code == 404:
            print('404 mf')
            return HttpResponse(api_request)

    return HttpResponse('Could not save data')


def select_random_game(gameList):
    index = randint(0, len(gameList) - 1)
    return gameList[index]