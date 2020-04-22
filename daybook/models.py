from django.db import models

from establishment.models import Establishment


class DayBook(models.Model):
    establishment = models.ForeignKey(to=Establishment, null=True, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
