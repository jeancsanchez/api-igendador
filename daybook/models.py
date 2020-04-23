from django.db import models

from establishment.models import Establishment


class DayBook(models.Model):
    establishment = models.ForeignKey(to=Establishment, null=True, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_day_book'
