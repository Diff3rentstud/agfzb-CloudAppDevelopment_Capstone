from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import models
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def django_view (request):
    return render(request,"index.html")


# Create an `about` view to render a static about page
# def about(request):
def about (request):
    if request.method == 'GET':
        return render(request,"djangoapp/about.html")
# ...


# Create a `contact` view to return a static contact page
#def contact(request):
def contact (request):
    if request.method == 'GET':
        return render(request,"djangoapp/contact.html")

# Create a `login_request` view to handle sign in request
# def login_request(request):
def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp/')
        else:
            return HttpResponseRedirect(reversed(viewname='djangoapp:login'))
    else:
        return render(request,'djangoapp/login')
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
def logout_request(request):
    if request.method == "GET":
        logout(request)
        messages.info(request,"Logged Out Done")

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
def registration_request(request):
    form = UserCreationForm()
    context ={}
    if request.method == "GET":
        return render(request,"djangoapp/registration.html",context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.debug("{} is new user".format(username))
        if not user_exist:
            user = User.objects.create_user(username=username, password=password)
            login(request,user)
            return redirect("djangoapp/")
        else:
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

