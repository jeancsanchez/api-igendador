from django.contrib import admin
from django.contrib.admin import register

from establishment.models import Establishment


@register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass
