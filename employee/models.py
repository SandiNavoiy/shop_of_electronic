from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Employee(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    phone = models.CharField(max_length=50, verbose_name="телефон", **NULLABLE)
    first_name = models.CharField(max_length=25, verbose_name="имя")
    last_name = models.CharField(max_length=25, verbose_name="фамилия", **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="активный")

    # переопределение поля user  как основного для идентификации на емаил
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"
