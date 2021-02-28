from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product


class Shop(ListView):
    model = Product

    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 12
