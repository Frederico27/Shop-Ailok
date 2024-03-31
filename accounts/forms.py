import django.contrib.auth.forms
from django.forms import ModelForm
from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields =  '__all__' #all field in the models
        # fields = ['cutomer'] #only specific form

class CreateUserForm(UserCreationForm):     
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
