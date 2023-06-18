from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment

def home(request):
    return render(request, 'healthcare/home.html')

@login_required
def book_appointment(request):
    # Add logic to retrieve available doctors
    # Example: doctors = Doctor.objects.all()
    # Pass the doctors to the template context
    context = {
        'doctors': ['Joy', 'Peter', 'David'],
    }
    return render(request, 'healthcare/book_appointment.html', context)


@login_required
def patient_profile(request, patient_name):
    context = {
        'patient_name': patient_name,
    }
    return render(request, 'healthcare/patient_profile.html', context)

@login_required
def doctor_profile(request, doctor_name):
    context = {
        'doctor_name': doctor_name,
    }
    return render(request, 'healthcare/doctor_profile.html', context)
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
    return render(request, 'healthcare/book_appointment.html', context)

def appointment_confirmation(request):
    return render(request, 'healthcare/appointment_confirmation.html')