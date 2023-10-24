from django.contrib import admin

from employee.models import Employee
from django.contrib import admin

# Register your models here.
@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')

