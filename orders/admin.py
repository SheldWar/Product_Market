from django.contrib import admin

from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'country', 'created_at', 'paid')
    list_filter = ('paid', 'created_at', 'updated_at')
    search_fields = ('email', 'phone')
    inlines = [OrderItemInline]
