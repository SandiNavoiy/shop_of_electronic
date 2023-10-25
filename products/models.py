from django.db import models

from employee.models import NULLABLE
from factory.models import Factory


# Create your models here.
class Product(models.Model):
    """Модель описание неких продкуктов"""
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=250, verbose_name='Модель', **NULLABLE)
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата выхода продукта')
    manufacturer = models.ForeignKey(Factory, on_delete=models.CASCADE,
                                     related_name='factory_product', verbose_name='Производитель')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации торара', **NULLABLE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title} {self.model}'

