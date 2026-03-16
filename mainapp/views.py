from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Category, Product, Review

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





# CRUD для Product
class ProductCreate(CreateView):
    model = Product
    fields = '__all__' 
    template_name = 'mainapp/generic_form.html'
    success_url = reverse_lazy('product_list') 

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'mainapp/generic_form.html'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'mainapp/generic_confirm_delete.html'
    success_url = reverse_lazy('product_list')

#CRUD для Category 
class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'mainapp/generic_form.html'
    success_url = reverse_lazy('product_list')

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'mainapp/generic_form.html'
    success_url = reverse_lazy('product_list')

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'mainapp/generic_confirm_delete.html'
    success_url = reverse_lazy('product_list')

#CRUD дя Review
class ReviewCreate(CreateView):
    model = Review
    fields = ['product', 'author', 'text']
    template_name = 'mainapp/generic_form.html'
    success_url = reverse_lazy('product_list')

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['text']
    template_name = 'mainapp/generic_form.html'
    success_url = reverse_lazy('product_list')

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'mainapp/generic_confirm_delete.html'
    success_url = reverse_lazy('product_list')