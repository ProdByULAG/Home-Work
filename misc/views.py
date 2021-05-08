from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from misc.models import Product


def product_detail(request):
    product = Product.objects.all()
    data = {
        'all_products' : product
    }
    return render(request, 'index.html', context=data)


def get_one_product(request, product_title):
    products = Product.objects.get(product_title=product_title)
    data = {
        'product': products
    }
    return render(request, 'detail.html', context=data)