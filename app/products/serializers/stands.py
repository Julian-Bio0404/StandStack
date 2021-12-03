"""Stand serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from app.products.models import Stand


class StandModelSerializer(serializers.ModelSerializer):
    """Stand model serializer."""

    class Meta:
        """Meta options."""
        model = Stand
        fields = '__all__'