from django.contrib import admin
from . models import *
# Register your models here.

MyModels = [Customer, Product, Order, OrderItem, ShippingAddress]
admin.site.register(MyModels)