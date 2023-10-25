# Generated by Django 4.2.6 on 2023-10-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_compani",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Название"
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                (
                    "building_number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Номер дома"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=50, unique=True, verbose_name="Email"),
                ),
                (
                    "type_organization",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Тип организации",
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        auto_now_add=True,
                        null=True,
                        verbose_name="Дата регистрации продавца",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
                "ordering": ("pk",),
            },
        ),
    ]
