from django.shortcuts import render, redirect, get_object_or_404
from . models import *

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def category_list(request):
    categories=Category.objects.all()
    return render(request, 'category_list.html', {'categories':categories})

def subcategory_list(request,category_slug):
    category=get_object_or_404(Category,slug=category_slug)
    subcategories=SubCategory.objects.filter(category=category)
    return render(request, 'subcategory_list.html', {'subcategories':subcategories, 'category':category})

def product_list(request,category_slug,subcategory_slug):
    subcategory=get_object_or_404(SubCategory,slug=subcategory_slug)
    products=Product.objects.filter(subcategory=subcategory)
    return render(request, 'product_list.html', {'subcategory':subcategory,'products':products})
