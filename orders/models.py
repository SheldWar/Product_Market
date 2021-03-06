from django.db import models

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=20, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Город')
    postal_code = models.CharField(max_length=20, verbose_name='Индекс')
    notes = models.CharField(max_length=250, blank=True, verbose_name='Комментарий к заказу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return f'Order {self.id}'

    class Meta:
        ordering = ('-created_at',)

        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Продукты')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во')

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)
