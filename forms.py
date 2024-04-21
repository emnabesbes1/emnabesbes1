from django import forms

 

from django.contrib.auth.forms import UserCreationForm

 

from django.contrib.auth.models import User

 


 

class UserRegistrationForm(UserCreationForm):

 

    email = forms.EmailField()

 


 

    class Meta:

 

        model = User

 

        fields = ['username', 'email', 'password1', 'password2']

 


 

class UserLoginForm(forms.Form):

 

    username = forms.CharField()

 

    password = forms.CharField(widget=forms.PasswordInput)

 


 

class ScanForm(forms.Form):

 

    scan_type = forms.CharField(label='Scan Type', max_length=100)

 

    target = forms.CharField(label='Target', max_length=100)
