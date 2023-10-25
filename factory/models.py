from django.db import models

from employee.models import NULLABLE


# Create your models here.
class Factory(models.Model):
    """ Модель описания производителя"""

    title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', **NULLABLE)
    phone = models.CharField(max_length=15, unique=True, verbose_name='Телефон', **NULLABLE)
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации производителя', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'