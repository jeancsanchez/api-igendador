from django.contrib import admin
from django.contrib.admin import register

from establishmentOwner.models import EstablishmentOwner


@register(EstablishmentOwner)
class EstablishmentOwnerAdmin(admin.ModelAdmin):
    pass
