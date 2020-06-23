from django.contrib import admin
from django.contrib.admin import register

from schedulingService.models import SchedulingService


@register(SchedulingService)
class SchedulingServiceAdmin(admin.ModelAdmin):
    pass
