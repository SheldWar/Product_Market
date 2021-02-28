from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogPosts.as_view(), name='blog'),
    path('detail/<str:slug>/', BlogDetail.as_view(), name='detail'),
    path('tag/<str:slug>/', Tags.as_view(), name='tag'),
    path('category/<str:slug>/', Category.as_view(), name='category'),
]
