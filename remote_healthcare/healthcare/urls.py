import statistics
from django.conf import settings
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

## migth overwrite the singles without the accounts
urlpatterns = [

    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),    path('dashboard/', views.dashboard, name='dashboard'),
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='healthcare/sign_in.html'), name='custom_login'), ## what happens after click sign in
    path('accounts/profile/', views.profile_view, name='profile'), ## where to fall after sso sign in
    path('accounts/', include('allauth.urls')),
    path('appointments/', views.appointments_view, name='appointments'),
    path('messages/', views.messages_view, name='messages'),
]