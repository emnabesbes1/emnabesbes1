from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
import requests
import json
from django.shortcuts import render
from .models import Vulnerability
from django.conf import settings

def BASE (request):
    return render(request,'base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def vulnerability_trends(request):
    # Retrieve vulnerability trend data (replace with your actual data retrieval logic)
    vulnerability_data = []  # List of tuples (timestamp, count)

    return render(request, 'dashboard.html', {'vulnerability_data': vulnerability_data})



def new_scan(request):
    # Add any logic here for initiating a new scan
    return render(request, 'new_scan.html')

