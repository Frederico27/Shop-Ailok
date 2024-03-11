from django.contrib import admin

# Register your models here.

#import some models
# from .models import Customer
from .models import Product, Tag

#import all models
from .models import *


#display title of column in admin template table
class accountsAdminCustomer(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'email', 'date_created')
    list_filter = ('name', 'phone', 'email', 'date_created')
    search_fields = ('name', 'phone', 'email', 'date_created')
    
class accountsAdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'Tag',  'date_created')
    list_filter = ('name', 'price', 'category', 'description',  'date_created')
    search_fields = ('name', 'price', 'category', 'description', 'date_created')
   
   #How to display many to many column to admin template table
    def Tag(self, request):
        product = Product.objects.get(id=request.id)
        tags = product.tags.all()
        
        tag_values = [tag.name for tag in tags] 
        return tag_values

class accountsAdminOrder(admin.ModelAdmin):
    list_display = ('customer', 'product', 'date_created','status')
    list_filter = ('customer', 'product', 'date_created','status')
    search_fields = ('customer', 'product','date_created','status')
    
class accountsAdminTags(admin.ModelAdmin):
    search_fields = ('name')
    list_display = ('name')
    list_filter = ('name')
    

admin.site.register(Customer, accountsAdminCustomer)
admin.site.register(Product, accountsAdminProduct)
admin.site.register(Order, accountsAdminOrder)
admin.site.register(Tag)


