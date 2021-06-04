from django.contrib import auth
from django.shortcuts import render, redirect
from misc.forms import CategoryForm, UserCreationForm, LoginForm, ProductForm

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
    return render(request, 'main.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/admin/')
        else:
            return render(request, 'register.html', context={'form': form})
    data = {
        'form': UserCreationForm
    }
    return render(request, 'register.html', context=data)


def login(request):
   if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                redirect('/')
                
                return render(request, 'layout.html', context={
                    'user': user,
                })

   return render(request, 'login.html', context={
       'form': LoginForm
   })


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_product(request):
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        form.save()
        redirect('/product/')
        return render(request, 'add_product.html')