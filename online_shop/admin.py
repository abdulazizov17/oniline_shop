from django.contrib import admin
# admin.py
from django.contrib import admin
from .models import Catagory, Product, Comment, Order

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Order)

# Register your models here.
