from django.contrib import admin
from django.contrib.admin import register

from calendarMonth.models import CalendarMonth


@register(CalendarMonth)
class CalendarMonthAdmin(admin.ModelAdmin):
    pass
