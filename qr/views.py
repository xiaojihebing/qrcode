from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('ok')

def DirectUrl(request, param1):
    tinyurl = param1
    from .models import Products
    product = Products.objects.filter(tinyurl__exact = tinyurl)
    if product:
        product = Products.objects.get(tinyurl = tinyurl)
        product_name = product.pro_name.strip()
        product_brand = product.pro_brand.strip()
        product_model = product.pro_model.strip()
        product_price  = product.pro_price.strip()
        product_capacity = product.pro_capacity.strip()
        product_company = product.pro_company.strip()
        product_url = product.pro_url.strip()
        product_weight = product.pro_weight.strip()
        product_input = product.pro_input.strip()
        product_output = product.pro_output.strip()
        product_add = product.pro_add.strip()
        product_phone = product.pro_phone.strip()
        product_color = product.pro_color.strip()
        product_size = product.pro_size.strip()        
        product_prointro = product.pro_intro
        product_comintro = product.com_intro
        return render_to_response('product.html',locals())
    else:
        return HttpResponse('sorry for no records')

