from datetime import datetime

from django.db import models

from establishmentOwner.models import EstablishmentOwner


class Establishment(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to=EstablishmentOwner, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_establishment'
