from django.db import models


# Create your models here.
from user.models import User
from vacancy.models import Vacancy


class Scheduling(models.Model):
    date_hours = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_scheduling'
