from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import * #import all (Product, Customer, Order, Tag)
from .forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
            else:
                # If form is invalid, display validation errors
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else:
            form = CreateUserForm()
            
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password= request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                
        
        context = {}
        
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'accounts/product.html', {'page_obj':page_obj})

@login_required(login_url='login')
def customer(request, pk_test):
    #tidak dapat object throw 404
    customer = get_object_or_404(Customer, id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    
    orders = myFilter.qs #orders Query Search
    
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer}) single form input
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        # form = OrderForm(request.POST)  single input post
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('customer', pk_test=order.customer.id)
    
    
    context = {'form': form}
    return render(request, 'accounts/order_form_update.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
