from django.shortcuts import render,redirect
import random
import json
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from food.secrets import apiKey,get_random
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm,UpdateUserForm,UpdateProfileForm
from django.contrib import messages
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
# def signup(request):
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("login")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = SignUpForm()
# 	return render (request=request, template_name="signup.html", context={"register_form":form})


def signup(request):
	form = SignUpForm()
	success = None
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form .is_valid():
			new_user = form.save(commit=False)
			subject = "Welcome to Mealplanner"
			message = f"Hello {new_user.username}, thank you for registering in Mealplanner App"
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [new_user.email, ]
			send_mail(subject,message,email_from,recipient_list)
			new_user.save()
			print(new_user)
			return redirect("login")
		if User.objects.filter(username=request.POST['username']).exists():
			error = "This username already exists"
			return render(request,"signup.html",{'form':form,"error":error})

		if User.objects.filter(email=request.POST['email']).exists():
			error = "This email is already taken"
			return render(request,"signup.html",{'form':form,"error":error})
		
	return render(request,"signup.html",{'form':form})


def login_request(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			print(user)
			return redirect("home")
		else:
			messages.success(request,"Sorry there was an error login In!! Try again...")
			return redirect("home")

	else:
		return render(request,"login.html",{})
		

def get_user(request):
	return User.objects.get(id=request.session['user_id'])

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='login')
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


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')