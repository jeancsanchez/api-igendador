from django.contrib import admin
from django.contrib.admin import register

from monthYear.models import MonthYear


@register(MonthYear)
class MonthYearAdmin(admin.ModelAdmin):
    pass
