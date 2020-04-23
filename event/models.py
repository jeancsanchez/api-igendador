from django.db import models

from daybook.models import DayBook
from user.models import User


class Event(models.Model):
    day_book = models.ForeignKey(to=DayBook, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    hour = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'tb_event'

    def __str__(self):
        return self.day_book.establishment.title + ' - ' + self.description

    def save(self, *args, **kwargs):
        if Event.objects.filter(day_book=self.day_book, hour=self.hour).exists():
            raise ValueError('There is already another event at this time.')
        return super(Event, self).save(*args, **kwargs)
