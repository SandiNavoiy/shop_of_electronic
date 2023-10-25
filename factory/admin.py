from django.contrib import admin
from factory.models import Factory


# Register your models here.
@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
