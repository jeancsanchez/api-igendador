from django.db import models


# Create your models here.
from establishment.models import Establishment


class Photo(models.Model):
    path = models.CharField(max_length=355, null=False)
    establishment = models.ForeignKey(to=Establishment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_photo'
