from django.contrib import admin
from django.urls import path
from accounts.views import login
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='products'),
    path('customer/<str:pk_test>', views.customer, name='customer'),
    path('createOrder/<str:pk>/', views.createOrder, name='create_order'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='update_order'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='delete_order'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
