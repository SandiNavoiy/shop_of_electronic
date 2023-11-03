from django.db import models

from employee.models import NULLABLE


# Create your models here.
class Link(models.Model):
    """Модель контактов прождажников"""

    name_compani = models.CharField(
        max_length=100, unique=True, verbose_name="Название"
    )  # Название компании
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    building_number = models.CharField(
        max_length=10, verbose_name="Номер дома", **NULLABLE
    )
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    type_organization = models.CharField(
        max_length=150, verbose_name="Тип организации", **NULLABLE
    )
    release_date = models.DateField(
        auto_now_add=True, verbose_name="Дата регистрации продавца", **NULLABLE
    )

    def __str__(self):
        return (
            f"Название компании {self.name_compani}, "
            f"Эл. адрес {self.email}, Город: {self.city}, Улица: {self.street}, Страна: {self.country}"
        )

    class Meta:
        ordering = ("pk",)
        verbose_name = "Контакты поставщика"
        verbose_name_plural = "Контакты поставщиков"
