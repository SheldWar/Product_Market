from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from .models import Product, Category


def product_list(request, category_slug=None):
    """Получаем список товаров, если в url есть категория - получаем по категории"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(availability=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    discounted_products = products.filter(discount__gt=0)

    return render(request, 'shop/shop.html', {'category': category, 'categories': categories, 'products': products,
                                              'discounted_products': discounted_products})


def product_detail(request, id, slug):
    """Страница детальной информации о продукте"""
    product = get_object_or_404(Product, id=id, slug=slug, availability=True)

    cart_product_form = CartAddProductForm()

    return render(request, 'shop/shop_details.html', {'product': product, 'cart_product_form': cart_product_form})

