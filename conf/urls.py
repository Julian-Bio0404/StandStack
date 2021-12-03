"""StandStack URL Configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app.products.urls', 'products'), namespace='stand-products')),
]
