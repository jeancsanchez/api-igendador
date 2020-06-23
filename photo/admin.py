from django.contrib import admin
from django.contrib.admin import register

from photo.models import Photo


@register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
