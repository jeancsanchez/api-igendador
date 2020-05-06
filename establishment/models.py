from django.db import models

from user.models import User


class Establishment(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_establishment'

    def __str__(self):
        return self.title


class Availability(models.Model):
    TYPES = (
        (0, 'Every day'),
        (1, 'Working days'),
        (2, 'Weekends'),
    )

    type = models.IntegerField(choices=TYPES)
    hour_opened = models.TimeField()
    hour_closed = models.TimeField()
    establishment = models.ForeignKey(to=Establishment, related_name='availabilities', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_availability'


class Photo(models.Model):
    path = models.CharField(max_length=300, blank=False, unique=True)
    establishment = models.ForeignKey(to=Establishment, related_name='photos', null=True, blank=False,
                                      on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_photo'
