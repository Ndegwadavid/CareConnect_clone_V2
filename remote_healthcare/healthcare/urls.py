# urls.py
from django.urls import path
from healthcare import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'healthcare'

urlpatterns = [
    path('', views.home, name='home'),
    #path('patient_profile/<str:patient_name>/', views.patient_profile, name='patient_profile'),
    #path('doctor_profile/<str:doctor_name>/', views.doctor_profile, name='doctor_profile'),
    path("book_appointment", views.book_appointment, name='book_appointment'),
    path("submit_appointment", views.submit_appointment, name='submit_appointment'),
    path("login.html", views.login, name="login"), ##added this route to facilitate login in
    path("register.html", views.register, name="register"),##register route
    ##adding for register and read more in due time
]
## these facilitates loading of the media and the static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)