from django.shortcuts import render
from django.http import HttpResponse
from .models import * #import all (Product, Customer, Order, Tag)

def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    
    total_customer = customer.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    
    context = {'orders': orders, 'customers': customer,
    'total_orders':total_orders, 'total_customer':total_customer, 
    'delivered':delivered, 'pending':pending}
    
    return render(request, 'accounts/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')
    
