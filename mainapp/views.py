from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

def product_list(request):
    products = Product.objects.select_related('category', 'farmer').all()
    context = {'products': products}
    return render(request, 'mainapp/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'mainapp/product_detail.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')