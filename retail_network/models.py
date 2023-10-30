from django.db import models

from links.models import Link
from products.models import Product

NULLABLE = {"blank": True, "null": True}


# Create your models here.
class Retail_network(models.Model):
    """Звено сети по продаже электроники"""

    title = models.CharField(max_length=50, verbose_name="Название")  # Название звена
    contacts = models.ForeignKey(
        Link, verbose_name="Контакты", on_delete=models.CASCADE
    )  # Контакты продавца
    products = models.ManyToManyField(Product, verbose_name="Продукты")  # Продукты
    debt = models.DecimalField(
        default=0,
        max_digits=21,
        decimal_places=2,
        verbose_name="Задолженность перед поставщиком",
        **NULLABLE,
        editable=False    # Запрет обновления поля через API
    )
    creation_time = models.DateTimeField(
        auto_now_add=True, verbose_name="время создания"
    )
    supplier = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="поставщик", **NULLABLE
    )
    release_date = models.DateField(
        auto_now_add=True, verbose_name="Дата регистрации звена продажи", **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "звено сети продажи"
        verbose_name_plural = "звенья сети продаж"
