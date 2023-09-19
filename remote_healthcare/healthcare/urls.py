import statistics
from django.conf import settings
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log-out/', views.log_out, name='log_out'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
path('accounts/login/', auth_views.LoginView.as_view(template_name='healthcare/sign_in.html'), name='custom_login'),
    path('accounts/', include('allauth.urls')),
]