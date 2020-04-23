from django.db import models


class Establishment(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    stars = models.FloatField(default=0)

    class Meta:
        db_table = 'tb_establishment'

    def __str__(self):
        return self.title


class Photo(models.Model):
    path = models.CharField(max_length=300, blank=False, unique=True)
    establishment = models.ForeignKey(to=Establishment, null=True, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tb_photo'
