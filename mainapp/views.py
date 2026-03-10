from django.shortcuts import render
from .data import products_db

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

def product_list(request):
    context = {'products': products_db}
    return render(request, 'mainapp/product_list.html', context)

def product_detail(request, product_id):
    product = next((item for item in products_db if item["id"] == product_id), None)
    context = {'product': product}
    return render(request, 'mainapp/product_detail.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')