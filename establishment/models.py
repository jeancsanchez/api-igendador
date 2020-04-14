from django.db import models

# Create your models here.
from location.models import Location


class Photo(models.Model):
    path = models.CharField(max_length=300, blank=False, unique=True)


class Establishment(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    location = models.OneToOneField(to=Location, on_delete=models.DO_NOTHING)
    photos = models.ForeignKey(Photo, on_delete=models.CASCADE)
