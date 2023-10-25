from django.contrib import admin
from django.db.models import QuerySet

from retail_network.models import Retail_network


# Register your models here.
@admin.register(Retail_network)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'debt')
    date_hierarchy = 'release_date'  # иерархия по датам
    actions = ('cancel_debt',)

    @admin.action(description='Сбросить задолженность')
    def cancel_debt(self, request, queryset: QuerySet):
        queryset.update(debt=0.00)
