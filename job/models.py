from django.db import models


# Create your models here.
from establishment.models import Establishment


class Job(models.Model):
    description = models.CharField(max_length=255, null=False)
    value = models.FloatField(default=0)
    time_minutes = models.IntegerField(default=0)
    comments = models.CharField(max_length=255, null=True)
    establishment = models.ForeignKey(to=Establishment, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_job'
