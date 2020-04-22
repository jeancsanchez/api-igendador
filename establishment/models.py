from django.db import models


class Establishment(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)


class Photo(models.Model):
    path = models.CharField(max_length=300, blank=False, unique=True)
    establishment = models.ForeignKey(to=Establishment, null=True, blank=False, on_delete=models.DO_NOTHING)
