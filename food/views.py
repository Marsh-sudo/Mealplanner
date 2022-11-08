from django.shortcuts import render
import random
import json
import requests
from django.http import HttpResponse,JsonResponse
from .secrets import apiKey,get_random

# Create your views here.
def search(request):
    query = request.GET.get('q')

    if query:
        results = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=10&apiKey={apiKey}")
        data =  results.json()
        
        # return HttpResponse(data.read())

    return render (request,'results.html',{"data":data['results'],"type":request.GET.get("type")})

def home(request):
    food = get_random()
    random_food = random.randrange(0, 3)
    recipe = food['recipes'][random_food]
    return render(request,'index.html',{"recipe":recipe})

def wines(request):
    return render(request,'wine.html')


def wines_pairing(request):
    query = request.GET.get('w')

    if query:
        results = requests.get(f"https://api.spoonacular.com/food/wine/recommendation?wine={query}&number=10&apiKey={apiKey}")
        data = results.json()

    return render (request,'wineSearch.html',{"data":data['recommendedWines']})