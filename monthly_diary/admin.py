from django.contrib import admin
from django.contrib.admin import register

from monthly_diary.models import CalendarMonth


@register(CalendarMonth)
class CalendarMonthAdmin(admin.ModelAdmin):
    pass
