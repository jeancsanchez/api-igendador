from django.db import models

from establishment.models import Vacancy, Job
from user.models import User


class Scheduling(models.Model):
    job = models.ManyToManyField(to=Job)
    date_hours = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_scheduling'
