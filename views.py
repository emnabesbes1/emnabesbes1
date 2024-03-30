from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
import requests
import json
from .models import Vulnerability
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login





def BASE (request):
    return render(request,'base.html')


def vulnerability_trends(request):
    # Retrieve vulnerability trend data (replace with your actual data retrieval logic)
    vulnerability_data = []  # List of tuples (timestamp, count)

    return render(request, 'dashboard.html', {'vulnerability_data': vulnerability_data})



def new_scan(request):
    # Add any logic here for initiating a new scan
    return render(request, 'new_scan.html')

 # Redirigez vers la page de connexion après la déconnexion



def login_view(request):
    error = None  # Initialisez la variable d'erreur à None

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("User:", username)
        print("User:", password)
        # Vérifiez si l'utilisateur existe dans Django
        User = authenticate(request, username=username, password=password)
        print("User:",User)
        
        


        if User is not None:
            # Si l'utilisateur existe, connectez-le
            login(request, User)
            return redirect('base')  # Redirigez vers home
        else:
            # Si l'utilisateur n'existe pas, définissez un message d'erreur
            error = 'INCORRECT USERNAME OR PASSWORD'

    # Affichez la page de connexion avec un éventuel message d'erreur
    return render(request, 'login.html', {'error': error})
