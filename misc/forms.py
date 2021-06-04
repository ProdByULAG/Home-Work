from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput

from misc.models import Category, Product


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=4, label="Введите имя категории",
                           widget=TextInput())

    def clean_name(self):
        category = Category.objects.filter(name=self.cleaned_data['name'])

        if len(category) != 0:
            raise ValidationError("Такакя категория уже есть!")
        else:
            return self.cleaned_data['name']


class UserCreationForm(forms.Form):

    username = forms.CharField(max_length=30,
                               widget=TextInput(attrs={
                                   "placeholder": "Nickname",
                                   'class': 'form-control'
                               }))
    password = forms.CharField(max_length=100,
                               widget=PasswordInput(attrs={
                                   'placeholder': 'Password',
                                   'class': 'form-control'
                               }))

    password1 = forms.CharField(max_length=100,
                                widget=PasswordInput(attrs={
                                    'placeholder': 'Repeat Password',
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('Такое имя уже существует')
        return username

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise ValidationError('Пароли не совпадают')
        return self.cleaned_data['password']

    def save(self, commit=True):
        username = self.cleaned_data["username"]
        user = User.objects.create(username=username,
                                   email='a@n.ru',
                                   password=self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):

    username = forms.CharField(max_length=30,
                               widget=TextInput(attrs={
                                   "placeholder": "Nickname",
                                   'class': 'form-control'
                               }))
    password = forms.CharField(max_length=100,
                               widget=PasswordInput(attrs={
                                   'placeholder': 'Password',
                                   'class': 'form-control'
                               }))

    def clean_username(self):
        user = User.objects.filter(username=self.cleaned_data['username'])

        if len(user) == 0:
            raise ValidationError("Введите корректные данные!")

        return self.cleaned_data['username']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        product = Product.objects.create(
            product_title=self.cleaned_data['product_title'],
            product_description=self.cleaned_data['product_description'],
            product_price=self.cleaned_data['product_price'],
            product_category_id=self.cleaned_data['product_category']
            )
        return product