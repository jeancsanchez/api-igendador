from django.db import models


# Create your models here.

from job.models import Job
from scheduling.models import Scheduling


class SchedulingService(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.DO_NOTHING)
    scheduling = models.ForeignKey(to=Scheduling, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_scheduling_service'
