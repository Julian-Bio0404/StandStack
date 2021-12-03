"""Product views."""

# Django REST framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from app.products.models import Product

# Serializers
from app.products.serializers import ProductModelSerializer, OrderProduct


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Product ViewSet.
    Handles list of the stand's products,
    retrieve a product or list product's options.
    """

    queryset = Product.objects.filter(available=True)
    serializer_class = ProductModelSerializer

    @action(detail=True)
    def options(self, request, *args, **kwargs):
        """List all product's options."""
        product = self.get_object()
        options = Product.objects.filter(
            name=product.name, available=True).values('options')
        data = {'options': [i.values() for i in options]}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def order(self, request, *args, **kwargs):
        """Order a product."""
        product = self.get_object()
        serializer = OrderProduct(
            data=request.data, context={'product': product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Successful order.'}
        return Response(data, status=status.HTTP_200_OK)
