from django.contrib import admin
from django.contrib.admin import register

from weekDay.models import WeekDay


@register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    pass
