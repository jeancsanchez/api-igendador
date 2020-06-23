from django.contrib import admin
from django.contrib.admin import register

from holiday.models import Holiday


@register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    pass
