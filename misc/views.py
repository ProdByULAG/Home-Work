from django.shortcuts import render
from misc.forms import CategoryForm


# Create your views here.
from misc.models import Product, Category, Review


def product_detail(request):
    product = Product.objects.all()
    data = {
        'all_products': product
    }

    for i in range(len(data['all_products'])):
        reviews = Review.objects.filter(review_product_id=data['all_products'][i].id)
        data['all_products'][i].col = len(reviews)


    return render(request, 'index.html', context=data)


def get_one_product(request, id):
    products = Product.objects.get(id=id)
    reviews = Review.objects.filter(review_product=products)
    data = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'detail.html', context=data)


def add_category(request):
    if request.method == "POST":
        categoryForm = CategoryForm(data=request.POST)

        if categoryForm.is_valid():
            Category.objects.create(name=request.POST.get('category'))
        else:
            return render(request, 'add_category.html', context={'form': categoryForm})

    return render(request, 'add_category.html', context={'form': CategoryForm})


def main_page(request):
    return None