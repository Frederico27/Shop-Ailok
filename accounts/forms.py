from django.forms import ModelForm
from django import forms
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields =  '__all__' #all field in the models
        # fields = ['cutomer'] #only specific form