import datetime

from django.db import models

from establishment.models import Establishment


class DayBook(models.Model):
    establishment = models.ForeignKey(to=Establishment, null=True, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'tb_day_book'

    def __str__(self):
        return self.date.strftime('%b %d %Y %H:%M:%S')
