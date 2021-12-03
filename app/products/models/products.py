"""Product models."""

# Django
from django.db import models


class Product(models.Model):
    """Product model."""

    OPTIONS = [
        ('XS', 'XS'), ('S', 'S'),
        ('M', 'M'), ('L', 'L'),
        ('XL', 'XL'),
    ]

    name = models.CharField(max_length=70)
    options = models.CharField(max_length=2, choices=OPTIONS)
    photo = models.ImageField(upload_to='products_photos', blank=True)
    available = models.BooleanField()
    amount = models.PositiveIntegerField()

    stand = models.ForeignKey('products.Stand', on_delete=models.CASCADE)

    def __str__(self):
        """Return product's name."""
        return self.name
