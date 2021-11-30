from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory
from .models.customer import Customer
from store import models



class AdminProduct(admin.ModelAdmin):
    list_display=["name",'price',"catagory"]


# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Catagory)
admin.site.register(Customer)
