from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import Shop

urlpatterns = [
    path('', Shop.as_view(), name='home'),
    path('<str:slug>', Shop.as_view(), name='shop_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
