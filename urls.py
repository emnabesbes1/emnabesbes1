from django.urls import path, include

 

from pages.zenmap_views import ZenmapScanView

 

from . import views

 

 


 


 

urlpatterns = [

 

     path('', views.login_view, name='login'),  # Page de connexion à la racine

 

     path('base/', views.BASE, name='BASE'),     # Page de base à /base/

 

     path('base/scan.html', views.new_scan, name='new_scan'),

 

     path('base/base.html', views.BASE, name='base'),

 

     path('base/user_page.html', views.user_page, name='user_page'),

     path('add/', views.add, name="add"),  # Add user page

   

    path("addrec/", views.addrec, name="addrec"),  # Add user form submission

   

    path('delete/<int:id>/', views.delete, name="delete"),  # Delete user

   

    path('update/<int:id>/', views.update, name="update"),

 

   

 

     #path('api/scans_in_progress/', scans_in_progress_view, name='scans_in_progress'),

 

     #path('new_scan/', views.new_scan, name='new_scan'),

 

     #path('zenmap/scan/', ZenmapScanView.as_view(), name='zenmap_scan'),

 

]
