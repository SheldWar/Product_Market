from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category

# Create your views here.


def blog_detail(request):
    return render(request, 'blog/blog-details.html')

class BlogPosts(ListView):
    model = Post
    template_name ='blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog/blog-details.html'
    context_object_name = 'post'

class Tags(ListView):
    model = Tag
    template_name = 'blog/blog.html'
    context_object_name = 'tags'


class Category(ListView):
    model = Category
    template_name = 'blog/blog.html'
    context_object_name = 'categories'

