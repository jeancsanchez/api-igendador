
from django.contrib import admin
from django.contrib.admin import register

from job.models import Job


@register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
