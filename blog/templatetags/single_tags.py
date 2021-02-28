from django import template

from blog.models import Tag, Category

register = template.Library()

@register.inclusion_tag('blog/tags.html')
def get_tags(cnt=10): #cnt - кол-во постов которые нужно выводить
    tags = Tag.objects.all()[:cnt]
    return {'tags': tags}

@register.inclusion_tag('blog/category_list.html')
def get_categories(cnt=10): #cnt - кол-во постов которые нужно выводить
    categories = Category.objects.all()[:cnt]
    return {'categories': categories}