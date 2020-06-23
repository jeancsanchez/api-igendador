from django.db import models

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    Birth_date = models.DateField()

    class Meta:
        db_table = 'tb_user'

