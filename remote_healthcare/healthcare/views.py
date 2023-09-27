from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

def home(request):
    return render(request, 'healthcare/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('sign_in')
    else:
        form = UserCreationForm()
    
    return render(request, 'healthcare/sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'healthcare/sign_in.html', {'form': form})

def profile_view(request): ## supports the fallback after sso
    return render(request, 'healthcare/dashboard.html')



@login_required
def dashboard(request):
    return render(request, 'healthcare/dashboard.html', {'user': request.user})


def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('sign_in')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'healthcare/password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'healthcare/password_reset_done.html'
