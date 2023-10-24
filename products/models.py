from django.db import models

from employee.models import NULLABLE


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=250, verbose_name='Модель', **NULLABLE)
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата выпуска')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title} {self.model}'

