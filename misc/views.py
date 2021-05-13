from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from misc.models import Product, Category


def product_detail(request):
    product = Product.objects.all()
    data = {
        'all_products': product
    }
    return render(request, 'index.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    data = {
        'product': product
    }
    return render(request, 'detail.html', context=data)
