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
        if self.kwargs:
            return Product.objects.filter(category__slug=self.kwargs['slug'])
        else:
            return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context
