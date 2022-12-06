from django.contrib import admin
from store_api.models import Product, ProductSize, Category, Order, OrderProductSize
# Register your models here.

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(ProductSize)
admin.site.register(Product)
admin.site.register(OrderProductSize)