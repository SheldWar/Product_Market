from django.db import models

"""
Product
==========
title, slug, photo, content, weight, price, availability, discount, created_at

Category
==========
title, slug
"""


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Транслит')
    photo = models.ImageField(upload_to='upload/product/photos/%Y/%m/%d/', verbose_name='Фото')
    content = models.TextField(verbose_name='Описание')
    weight = models.FloatField(verbose_name='Вес')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    availability = models.BooleanField(verbose_name='Наличие')
    discount = models.IntegerField(default=0, verbose_name='Скидка в %')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    def get_sale(self):
        """Расчитываем стоимость со скидкой"""
        return self.price * (100 - self.discount) / 100

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        ordering = ('title',)
        index_together = (('id', 'slug'),)


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Транслит')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
