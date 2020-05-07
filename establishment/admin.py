from django.contrib import admin
from django.contrib.admin import register

from establishment.models import Establishment, Photo, Availability


class PhotoInline(admin.StackedInline):
    model = Photo


class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 2
    verbose_name_plural = 'Aval'


@register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    inlines = [AvailabilityInline, PhotoInline, ]
