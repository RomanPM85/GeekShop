from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context = {
            'categories': ProductCategory.objects.all(),
            'products': products,
        }
    else:
        context = {
            'categories': ProductCategory.objects.all(),
            'products': Product.objects.all(),
        }
    return render(request, 'mainapp/products.html', context)
