import requests
import json

apiKey = "332a8c3baef140dab8cb40493a0990bc"

def get_random():
    response = requests.get(f"https://api.spoonacular.com/recipes/random?number=5&tags=main+course&apiKey={apiKey}")
    return response.json()