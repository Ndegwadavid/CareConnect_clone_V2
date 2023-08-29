from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

##added these functions for home and login 
##addding for register in due time 
def home(request):
    return render(request, "healthcare/home.html")

def login(request):
    return render(request, "healthcare/login.html")

def readmore(request):
    return render(request,"healthcare/readmore.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Pass POST data to form to prevent failing csrf
        if form.is_valid():
            form.save()
            return redirect("login.html")
    else:
        form = UserCreationForm()
    return render(request, "healthcare/register.html", {"form": form})
