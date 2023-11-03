from django.contrib import admin
from django.db.models import QuerySet

from retail_network.models import Retail_network


# Register your models here.
@admin.register(Retail_network)
class RetailAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "contacts",
        "debt",
        "get_email",
    )
    date_hierarchy = "release_date"
    list_filter = ("contacts__city",)  # Фильтр по полю city
    actions = ("cancel_debt",)

    # Определение уникальных значений городов
    def get_city_choices(self, request):
        """Определение уникальных значений городов"""
        return Retail_network.objects.values_list(
            "contacts__city", flat=True
        ).distinct()

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        """настройки виджета и выбора полей результатов в админке Django"""
        if db_field.name == "contacts__city":
            kwargs["choices"] = self.get_city_choices(request)
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    @admin.action(description="Сбросить задолженность")
    def cancel_debt(self, request, queryset: QuerySet):
        queryset.update(debt=0.00)

    def get_email(self, obj):
        return obj.contacts.email if obj.contacts else ""

    get_email.short_description = "Email"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("contacts")
