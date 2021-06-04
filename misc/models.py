from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    product_title = models.CharField(max_length=50, verbose_name='Название продукта')
    product_description = models.TextField('Описание продукта')
    product_price = models.IntegerField('Цена продукта')
    product_category = models.ForeignKey(Category, verbose_name='Категория продукта', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    review_author = models.CharField(max_length=20, null=True, verbose_name='Автор')
    review_text = models.TextField('Отзыв')
    review_updated = models.DateTimeField(auto_now=True)
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_author














