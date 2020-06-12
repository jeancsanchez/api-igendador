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
