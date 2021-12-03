"""Stand model."""

# Django
from django.db import models


class Stand(models.Model):
    """Stand model."""

    name = models.CharField(max_length=70, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        """Return stand's name."""
        return self.name