from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from .filters import ProductFilter
from django.contrib import messages
import django_filters
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def products(request):
    products = ProductFilter(request.GET, queryset=Product.objects.all())
    ctx = {"products": products}    
    return render(request, 'products/products.html',ctx)

def my_products(request):
    products = Product.objects.filter(user=request.user)
    products = ProductFilter(request.GET, queryset=products)
    ctx = {"products": products}    
    return render(request, 'products/my_products.html',ctx)

@login_required
def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            product = form.save(commit=False)           # Create a new product object but don't save it yet
            product.user = request.user                 # Set the user to the current user
            product.save()                              # Save the new product object
            messages.success(request, 'Product added successfully')
            return redirect('products')
        else:
            messages.error(request, 'Error adding product')
    ctx = {"form": form}
    return render(request, 'products/add_product.html', ctx)

def view_product(request, pid):
    product = get_object_or_404(Product, pk=pid)
    ctx = {"product": product}
    return render(request, 'products/view_product.html', ctx)

@login_required
def edit_product(request, pid):
    product = get_object_or_404(Product, pk=pid)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('products')
        else:
            messages.error(request, 'Error updating product')
    ctx = {"form": form}
    return render(request, 'products/edit_product.html', ctx)

@login_required
def delete_product(request, pid):
    product = get_object_or_404(Product, pk=pid)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products')