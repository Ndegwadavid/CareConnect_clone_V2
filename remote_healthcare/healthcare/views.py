from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment
from django.shortcuts import render
from django.contrib.auth import authenticate, login


##added these functions for home and login 
##addding for register in due time 
def home(request):
    return render(request, "healthcare/home.html")

def login(request):
    return render(request, "healthcare/login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Create a new user with the submitted username and password respectively
        user = User.objects.create_user(username=username, password=password)
        #user logining in
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('success')
    
    return render(request, "healthcare/register.html")
@login_required
def book_appointment(request):
    context = {
        'doctors': ['Joy', 'Peter', 'David'],
    }
    return render(request, 'book_appointment.html', context)

def my_view(request):
    return render(request, 'remote_healthcare/home.html', {'css_file': 'remote_healthcare/css/my_css_file.css'})



@login_required
def patient_profile(request, patient_name):
    context = {
        'patient_name': patient_name,
    }
    return render(request, 'patient_profile.html', context)

@login_required
def doctor_profile(request, doctor_name):
    context = {
        'doctor_name': doctor_name,
    }
    return render(request, 'doctor_profile.html', context)
def submit_appointment(request):
    if request.method == 'POST':
        # Retrieve form data
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Create appointment for the sick person
        appointment = Appointment(doctor=doctor, date=date, time=time, message=message)
        appointment.save()


        # Redirect the user to a confirmation for appointment
        return redirect('healthcare:appointment_confirmation')

    # if not POST request, render the form again
    context = {
        'doctors': ['Joy', 'Peter', 'David'],
    }
    return render(request, 'book_appointment.html', context)

def appointment_confirmation(request):
    return render(request, 'appointment_confirmation.html')