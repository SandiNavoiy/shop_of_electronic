from django.contrib import admin
from factory.models import Factory


# Register your models here.
@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    date_hierarchy = 'release_date'   # иерархия по датам
    list_display_links = ('title',)
    empty_value_display = "Отсутствует"
