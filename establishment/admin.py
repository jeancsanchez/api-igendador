from django.contrib import admin

# Register your models here.
from establishment.models import Establishment, Availability, Photo

admin.site.register(Establishment)
admin.site.register(Availability)
admin.site.register(Photo)
