from django.shortcuts import render

# Create your views here.

def index(request):
    content = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', content)

def products(request):
    content = {
        'title': 'geekShop - catalog'
    }
    return render(request, 'mainapp/products.html', content)