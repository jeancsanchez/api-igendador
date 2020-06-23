import datetime

from django.db import models

from establishment.models import Vacancy


class MonthlyDiary(models.Model):
    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )

    WEEKDAYS = (
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
        (5, 'Thursday'),
        (6, 'Friday'),
        (7, 'Saturday'),
    )

    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    is_open = models.BooleanField(default=False)
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.DO_NOTHING)
    month_year = models.IntegerField(choices=MONTHS, default=1)
    weekday = models.IntegerField(choices=WEEKDAYS, default=1)
    year = models.IntegerField(default=datetime.datetime.today().year)

    class Meta:
        unique_together = (('vacancy', 'weekday', 'month_year', 'year',),)
        db_table = 'tb_monthly_diary'


class Holiday(models.Model):
    day = models.DateField(null=False)
    name_holiday = models.CharField(max_length=255, null=False)
    monthly_diary = models.ForeignKey(to=MonthlyDiary, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_holiday'
