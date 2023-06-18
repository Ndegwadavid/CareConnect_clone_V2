from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # patients more details required 

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # more details for doctor 

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
def __str__(self):
        return f'Appointment with {self.doctor} on {self.date} at {self.time}'

