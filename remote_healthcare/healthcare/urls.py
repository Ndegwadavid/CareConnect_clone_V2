# urls.py
from django.urls import path
from healthcare import views

app_name = 'healthcare'

urlpatterns = [
    path('', views.home, name='home'),
    path('patient_profile/<str:patient_name>/', views.patient_profile, name='patient_profile'),
    path('doctor_profile/<str:doctor_name>/', views.doctor_profile, name='doctor_profile'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('submit_appointment/', views.submit_appointment, name='submit_appointment'),
    #path('cancel_appointment/', views.cancel_appointment, name='cancel_appointment'), uncomment when attribute 'cancel_appointment' is added to healthcare.views
]
