from django.contrib import admin

# Register your models here.

#import some models
# from .models import Customer

#import all models
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)


