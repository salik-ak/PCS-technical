from django.contrib import admin

from .models import Category, Product, Banner, Cart, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Banner)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
