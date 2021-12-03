"""Products models admin."""

# Django
from django.contrib import admin

# Models
from app.products.models import Stand, Product


@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    """Stand model admin."""

    list_display = [
        'pk','name',
        'qr_code'
    ]

    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product model admin."""

    list_display = [
        'pk', 'name',
        'options', 'stand',
        'available', 'amount'
    ]

    search_fields = [
        'stand__name', 'name',
    ]

    list_filter = ['stand__name', 'available']
