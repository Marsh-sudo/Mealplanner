import requests
import json

apiKey = "Api key"

def get_random():
    response = requests.get(f"https://api.spoonacular.com/recipes/random?number=5&tags=main+course&apiKey={apiKey}")
    return response.json()