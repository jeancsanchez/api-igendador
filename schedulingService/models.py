from django.db import models


# Create your models here.
from establishment.models import Scheduling
from job.models import Job


class SchedulingService(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.DO_NOTHING)
    scheduling = models.ForeignKey(to=Scheduling, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_scheduling_service'
