from django.contrib import admin
from .models import Product, Image, Order, Favourite


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Favourite)