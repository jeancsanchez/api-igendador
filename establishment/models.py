from django.db import models

from user.models import UserEstablishmentOwner


class Establishment(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to=UserEstablishmentOwner, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_establishment'


class Job(models.Model):
    description = models.CharField(max_length=255, null=False)
    value = models.FloatField(default=0)
    time_minutes = models.IntegerField(default=0)
    comments = models.CharField(max_length=255, null=True)
    establishment = models.ForeignKey(to=Establishment, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_job'


class Vacancy(models.Model):
    establishment = models.ForeignKey(to=Establishment, on_delete=models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_vacancy'


class Photo(models.Model):
    path = models.CharField(max_length=355, null=False)
    establishment = models.ForeignKey(to=Establishment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_photo'
