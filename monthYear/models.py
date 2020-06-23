from django.db import models


# Create your models here.
class MonthYear(models.Model):
    name_month = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tb_monthYear'
