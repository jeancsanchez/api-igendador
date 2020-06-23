from django.contrib import admin
from django.contrib.admin import register

from monthly_diary.models import MonthlyDiary


@register(MonthlyDiary)
class MonthlyDiaryAdmin(admin.ModelAdmin):
    pass
