from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    birth_date = models.DateField()

    class Meta:
        db_table = 'tb_user'


class UserEstablishmentOwner(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)

    class Meta:
        db_table = 'tb_user_establishment_owner'
