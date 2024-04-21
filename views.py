from django.contrib.auth import login, authenticate

 

from django.shortcuts import render, redirect

 

import os

 

from django.shortcuts import render

 

from django.http import JsonResponse

 

import requests

 

from pages.forms import ScanForm

 

from django.shortcuts import render

 

from .models import User,Role

from django.http import HttpResponseNotFound

 


 

def login_view(request):    #login

 

    error = None

 


 

    if request.method == "POST":

 

        username = request.POST.get('username')

 

        password = request.POST.get('password')

 


 

        # Print username and password

 

        print("Username:", username)

 

        print("Password:", password)

 


 

        user = authenticate(request, username=username, password=password)

 

        print("User:", user)  # Print the authenticated user

 

        if user :

 

            login(request, user)

 

            return redirect('BASE')  # Redirect to home after successful login

 

        else:

 

            error = 'INCORRECT USERNAME OR PASSWORD'

 

   

 

    # Handle GET request here

 

    return render(request, 'login.html', {'error': error})

 


 


 

def BASE(request):

 

    return render(request, 'base.html')

 


 

def vulnerability_trends(request):   #dashbord

 

    # Retrieve vulnerability trend data (replace with your actual data retrieval logic)

 

    vulnerability_data = []  # List of tuples (timestamp, count)

 

    return render(request, 'base.html', {'vulnerability_data': vulnerability_data})

 


 

def new_scan(request):

 

    if request.method == 'GET':

 

        form = ScanForm()

 

        return render(request, 'scan.html', {'form': form})

 


 

    elif request.method == 'POST':

 

        form = ScanForm(request.POST)

 

        if form.is_valid():

 

            scan_result = print('hello')

 

            if scan_result:

 

                return JsonResponse({'message': 'Scan started successfully.'})

 

            else:

 

                return JsonResponse({'error': 'Failed to start the scan.'}, status=500)

 

        else:

 

            return render(request, 'scan.html', {'form': form})

       

        

        

        

#acces au nessus via son url

 

#def new_scan(request):

 

    # Rediriger vers l'URL de votre instance Nessus Essentials

 

    #return redirect('https://192.168.110.144:8834')

def user_page(request):

    mem=User.objects.all()

    return render(request,'user_page.html',{'mem':mem})

 

def add(request):

    return render(request, 'add.html')

 

def addrec(request):

    if request.method == 'POST':

        x = request.POST.get('name')

        y = request.POST.get('email')

        z = request.POST.get('password')

        w = request.POST.get('role_id')  # Assuming 'role_id' is the name of the field containing the role ID

 

        # Assuming 'role' is the ForeignKey field in your User model

        # You need to get the Role object based on the provided role ID

        try:

            role = Role.objects.get(pk=w)

        except Role.DoesNotExist:

            return HttpResponseNotFound("Role ID does not exist")

 

        # Create and save the new User object

        mem = User.objects.create(user_name=x, email=y, password=z, role=role)

 

        return redirect("/")

    else:

        # Handle GET request if needed

        pass

 

def delete(request, id):

    mem = User.objects.get(id=id)

    mem.delete()

    return redirect("/")

 

def update(request, id):

    mem = User.objects.get(id=id)

    return render(request, 'update.html', {'mem': mem})

 

def uprec(request, id):

    if request.method == 'POST':

        x = request.POST.get('name')

        y = request.POST.get('email')

        z = request.POST.get('password')

        w = request.POST.get('role_id')

       

        # Assuming 'role' is the ForeignKey field, you need to get the Role object

        # You may need to adjust this part based on how you handle roles in your application

        role = Role.objects.get(id=w)

 

        # Update the existing User object

        mem = User.objects.get(id=id)

        mem.user_name = x

        mem.email = y

        mem.password = z

        mem.role = role

        mem.save()

 

        return redirect("/")

    else:

        # Handle GET request if needed

        pass



