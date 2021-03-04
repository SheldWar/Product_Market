from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'weight', 'price', 'discount', 'category', 'availability', 'created_at', 'updated_at')
    list_filter = ('availability', 'created_at', 'updated_at')
    list_editable = ('price', 'availability')
    prepopulated_fields = {'slug': ('title',)}
