from django.db import models

from daybook.models import DayBook


class Event(models.Model):
    day_book = models.ForeignKey(to=DayBook, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    hour = models.TimeField(auto_now=True)
