from django.db import models


# Create your models here.
from establishment.models import Establishment


class Vacancy(models.Model):
    establishment = models.ForeignKey(to=Establishment, on_delete=models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_vacancy'
