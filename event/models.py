from django.db import models

from establishment.models import Establishment
from user.models import User


class Event(models.Model):
    establishment = models.ForeignKey(to=Establishment, on_delete=models.PROTECT)
    client = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_event'

    def __str__(self):
        return self.establishment.__str__() + ' | ' + self.description + ' | ' + self.client.name

    def save(self, *args, **kwargs):
        if Event.objects.filter(establishment=self.establishment, data=self.data).exists():
            raise ValueError('There is already another event at this time.')
        return super(Event, self).save(*args, **kwargs)
