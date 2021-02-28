from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Author, Category, Tag

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','get_photo','views')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='80'>")
        return '-'

    get_photo.short_description = "Превью"

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','lastname', 'author_status')
    list_display_links = ('id', 'name','lastname')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)