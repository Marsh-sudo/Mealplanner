from django.shortcuts import render,redirect
import random
import json
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from .secrets import apiKey,get_random
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm,LoginUserForm
from django.contrib import messages

# Create your views here.
def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignUpForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = LoginUserForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print(user)
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = LoginUserForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  
#             # load the profile instance created by the signal
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')

#             # login user after signing up
#             user = authenticate(username=username, password=password)
#             login(request, user)

#             # redirect user to home page
#             return redirect('home')
    
#     form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

def search(request):
    query = request.GET.get('q')

    if query:
        results = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=10&apiKey={apiKey}")
        data =  results.json()
        
        # return HttpResponse(data.read())

    return render (request,'results.html',{"data":data['results'],"type":request.GET.get("type")})

@login_required(login_url='login')
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