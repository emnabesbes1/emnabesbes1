from xml.etree.ElementInclude import include
from django.urls import path, include 
from . import views



urlpatterns = [
    path('', views.login_view, name='login'),
    path('', views.BASE, name='BASE'),
    path('new-scan/', views.new_scan, name='new-scan'),
   
    
]
