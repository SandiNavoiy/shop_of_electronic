from django.core.management import BaseCommand

from employee.models import Employee


# кастомная команда для создания суперUser
class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = Employee.objects.create(
            email="2@admin.ru",
            first_name="Admin",
            last_name="Admin",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        admin.set_password("spartak67")  # установка пароля
        admin.save()  # сохраниние в БД
