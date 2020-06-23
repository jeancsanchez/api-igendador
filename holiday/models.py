from django.db import models


# Create your models here.
from calendarMonth.models import CalendarMonth


class Holiday(models.Model):
    day = models.DateField(null=False)
    name_holiday = models.CharField(max_length=255, null=False)
    calendar_month = models.ForeignKey(to=CalendarMonth, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_holiday'

