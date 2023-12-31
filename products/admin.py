from django.contrib import admin

from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "model", "release_date")
    date_hierarchy = "release_date"  # иерархия по датам
