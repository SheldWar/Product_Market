from django.contrib import admin

from .models import Post, Author, Category, Tag

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created_at','photo','views','category','tags','author')
    list_display_links = ('id', 'title')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','lastname', 'author_status')
    list_display_links = ('id', 'name','lastname')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_display_links = ('id', 'title')

class TagAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_display_links = ('id', 'title')



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)