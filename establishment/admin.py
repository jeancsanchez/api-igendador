from django.contrib import admin
from django.contrib.admin import register

from scheduling.models import Scheduling


@register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    pass
