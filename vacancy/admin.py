from django.contrib import admin
from django.contrib.admin import register

from vacancy.models import Vacancy


@register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
