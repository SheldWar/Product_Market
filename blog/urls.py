from django.urls import path, include

from .views import blog, blog_detail

urlpatterns = [
    path('', blog),
    path('detail/', blog_detail),
]