from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'price', 'stock', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug' : ('prod_name',)}

admin.site.register(Product, ProductAdmin)
