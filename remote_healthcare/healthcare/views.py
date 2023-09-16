from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "healthcare/home.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard') 
        else:
            
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, "healthcare/login.html", {"form": form})

def dashboard(request):
    return render(request, "healthcare/dashboard.html")

def readmore(request):
    return render(request,"healthcare/readmore.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Pass POST data to form to prevent failing csrf
        if form.is_valid():
            form.save()
            return redirect("dashboard.html")
    else:
        form = UserCreationForm()
    return render(request, "healthcare/register.html", {"form": form})

def logout(request):
    messages.sucess(request, "logged out successfully")
