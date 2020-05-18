from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import QuestionForm
#from .models import PhoneBook
from django.http import HttpResponse

# Create your views here.
def login(response):
    if response.method == "POST":
        form = QuestionForm(response.POST)
        if form.is_valid():
            first_name = response.POST['first_name']
            last_name = response.POST['last_name']
            phone_number = response.POST['phone_number']
            # contact = PhoneBook.objects.create(first_name=first_name, 
            #                                     last_name=last_name, 
            #                                     phone_number=phone_number)
            json = {"first_name":first_name, "last_name": last_name, "phone_number": phone_number}
            form.save(json)
            return render(response, "home.html")
    else:
        form = QuestionForm()
    return render(response, "login/login.html", {"form":form})

def home(response):
    return render(response, "home.html")