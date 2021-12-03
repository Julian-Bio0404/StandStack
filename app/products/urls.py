"""Products URLs."""

# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from app.products.views import ProductViewSet, StandViewSet


router = DefaultRouter()
router.register(r'stands', StandViewSet, basename='stands')

router.register(
    r'stands/(?P<id>[0-9]+)/products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]