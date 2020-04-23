from django.db import models
from unidecode import unidecode

from establishment.models import Establishment


class Location(models.Model):
    latitude = models.FloatField(null=True, default=0)
    longitude = models.FloatField(null=True, default=0)
    cep = models.CharField(null=True, max_length=30)
    country = models.CharField(null=True, max_length=30, default='Brasil')
    state = models.CharField(null=True, max_length=40, default='Ceara')
    city = models.CharField(null=True, max_length=150, default='Fortaleza')
    neighborhood = models.CharField(null=True, blank=True, max_length=150)
    street = models.CharField(null=True, blank=True, max_length=150)
    number = models.CharField(null=True, blank=True, max_length=10)
    establishment = models.ForeignKey(to=Establishment, related_name='locations', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_location'

    def __str__(self):
        address = ''

        if self.street:
            address += self.street + ','

        if self.number:
            address += self.number + '-'

        if self.neighborhood:
            address += self.neighborhood + '/'

        return address + self.city + ' (' + self.state + ')'

    def save(self, *args, **kwargs):
        if self.country:
            self.country = unidecode(self.country.upper())

        if self.state:
            self.state = unidecode(self.state.upper())

        if self.city:
            self.city = unidecode(self.city.title())

        if self.neighborhood:
            self.neighborhood = unidecode(self.neighborhood.title())

        if self.street:
            self.street = unidecode(self.street.title())

        if self.number:
            self.number = unidecode(self.number)

        super(Location, self).save(*args, **kwargs)
