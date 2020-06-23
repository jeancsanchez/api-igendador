from django.db import models


# Create your models here.
class EstablishmentOwner(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)

    class Meta:
        db_table = 'tb_establishment_owner'
