from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from webproj_api.models import Game, GameImages, GameDescription, GameDetails
import json

# Create your views here.

@csrf_exempt
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_json = [game.to_json() for game in games]
        return JsonResponse(game_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            games = Game.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(games.to_json())

@csrf_exempt
def game_details(request, game_id):
    try:
        details = Game.objects.all().select_related('images', 'description', 'details').get(id=game_id)
    except Game.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(details.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        details.name = data['name']
        details.thumbnail = data['thumbnail']
        details.background_img = data['background_img']
        details.screenshot1 = data['screenshot1']
        details.screenshot2 = data['screenshot2']
        details.screenshot3 = data['screenshot3']
        details.screenshot4 = data['screenshot4']
        details.description = data['description']
        details.website_url = data['website_url']
        details.publisher = data['publisher']
        details.platforms = data['platforms']
        details.likes = data['likes']
        details.dislikes = data['dislikes']
        details.release_date = data['release_date']
        details.genres = data['genres']
        details.metacritic_points = data['metacritic_points']
        details.save()
        return JsonResponse(details.to_json())
    elif request.method == 'DELETE':
        details.delete()
        return JsonResponse({'message': 'deleted'}, status=204)