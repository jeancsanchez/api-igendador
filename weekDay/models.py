from django.db import models


# Create your models here.
class WeekDay(models.Model):
    name_day = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tb_weekDay'
