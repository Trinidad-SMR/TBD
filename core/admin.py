from django.contrib import admin
from .models import *
from .models import Category, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Venta)
