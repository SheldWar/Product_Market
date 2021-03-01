from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, Category


class Shop(ListView):
    model = Product

    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        """Если выбрали категорию, то делаем выборку по категории"""
        if self.kwargs:
            return Product.objects.filter(discount=0, category__slug=self.kwargs['slug'])
        else:
            return Product.objects.filter(discount=0)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        # если выбрали категорию, ищем товары со скидкой в категории
        if self.kwargs:
            context['discounted_products'] = Product.objects.filter(discount__gt=0, category__slug=self.kwargs['slug'])
        else:
            context['discounted_products'] = Product.objects.filter(discount__gt=0)

        return context
