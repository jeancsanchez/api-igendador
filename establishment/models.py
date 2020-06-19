from datetime import datetime

from django.db import models


class EstablishmentOwner(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)

    class Meta:
        db_table = 'tb_establishment_owner'


class Establishment(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to=EstablishmentOwner, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_establishment'


class Photo(models.Model):
    path = models.CharField(max_length=355, null=False)
    establishment = models.ForeignKey(to=Establishment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_photo'


class Job(models.Model):
    description = models.CharField(max_length=255, null=False)
    value = models.FloatField(default=0)
    time_minutes = models.IntegerField(default=0)
    comments = models.CharField(max_length=255, null=True)
    establishment = models.ForeignKey(to=Establishment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_job'


class Vacancy(models.Model):
    scheduling = models.ForeignKey(to=Establishment, on_delete=models.CASCADE)
    comments = models.TextFiel(blank=True, null=True)

    class Meta:
        db_table = 'tb_vacancy'


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    Birth_date = models.DateField()

    class Meta:
        db_table = 'tb_user'


class Scheduling(models.Model):
    date_hours = models.DateTimeField()
    comments = models.TextFiel(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_scheduling'


class SchedulingService(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE)
    scheduling = models.ForeignKey(to=Scheduling, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_scheduling_service'


class WeekDay(models.Models):
    name_day = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tb_weekDay'


class MonthYear(models.Models):
    name_month = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tb_monthYear'


class CalendarMonth(models.Models):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    open = models.enumfield()
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.CASCADE)
    weekDay = models.ForeignKey(to=WeekDay, on_delete=models.CASCADE)
    monthYear = models.ForeignKey(to=MonthYear, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_calendarMonth'


class Holiday(models.Models):
    day = models.DateField(null=False)
    name_holiday = models.CharField(max_length=255, null=False)
    calendar_month = models.ForeignKey(to=CalendarMonth, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_holiday'
