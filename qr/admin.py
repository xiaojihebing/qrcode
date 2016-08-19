from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce.js',  
            '/static/js/tiny_mce/textareas.js',
        )
    list_display = ('tinyurl','pro_name','pro_brand','pro_model', 'pro_price', 'pro_company')
    search_field = ('pro_model',)
    list_filter = ('pro_model', 'pro_brand',)

admin.site.register(Products, ProductsAdmin)
