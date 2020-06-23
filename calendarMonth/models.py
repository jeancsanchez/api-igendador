from django.db import models


# Create your models here.
from monthYear.models import MonthYear
from vacancy.models import Vacancy
from weekDay.models import WeekDay


class CalendarMonth(models.Model):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    open = models.BooleanField(default=False)
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.DO_NOTHING)
    weekDay = models.ForeignKey(to=WeekDay, on_delete=models.DO_NOTHING)
    monthYear = models.ForeignKey(to=MonthYear, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_calendarMonth'
