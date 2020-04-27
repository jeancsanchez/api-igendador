from django.db import models
from django.utils import timezone

from establishment.models import Establishment


class DayBook(models.Model):
    establishment = models.ForeignKey(to=Establishment, null=True, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tb_day_book'
        ordering = ('date',)

    def __str__(self):
        return self.establishment.title + ' | ' + self.date.strftime('%d/%m/%Y | %H:%M')
