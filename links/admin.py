from django.contrib import admin

from links.models import Link


# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("name_compani", "country", "city", "email")
    date_hierarchy = 'release_date'  # иерархия по датам
    list_filter = ('country', 'city')
