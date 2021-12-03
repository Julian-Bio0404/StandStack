"""Product serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from app.products.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer."""

    class Meta:
        """Meta options."""
        model = Product
        fields = '__all__'


class OrderProduct(serializers.Serializer):

    option = serializers.CharField(max_length=2)

    def validate(self, data):
        """Verify that option is available."""
        product_name = self.context['product'].name
        products = Product.objects.filter(
            name=product_name, options=data['option'], available=True)

        if not products.exists():
            raise serializers.ValidationError(
                f'this option is not available for this product.')
        return data

    def save(self):
        """Update the product."""
        product = self.context['product']
        product.amount -= 1
        product.save()
        return product