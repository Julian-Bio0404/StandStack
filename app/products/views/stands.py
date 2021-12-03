"""Stand views."""

# Django REST framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from app.products.models import Stand

# Serializers
from app.products.serializers import StandModelSerializer


class StandViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    Stand ViewSet.
    Handles list of the stands or retrieve a stand.
    """

    queryset = Stand.objects.all()
    serializer_class = StandModelSerializer
