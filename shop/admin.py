from django.contrib import admin

from .models import Category, Product


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'weight', 'price', 'discount', 'category', 'availability', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, AdminProduct)


class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, AdminCategory)
