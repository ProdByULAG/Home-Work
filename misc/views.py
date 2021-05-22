from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from misc.models import Product, Category, Review


def product_detail(request):
    product = Product.objects.all()
    data = {
        'all_products': product
    }
    return render(request, 'index.html', context=data)


def get_one_product(request, id):
    products = Product.objects.get(id=id)
    reviews = Review.objects.filter(product__id=id)
    data = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'detail.html', context=data)
