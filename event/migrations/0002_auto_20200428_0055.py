# Generated by Django 3.0.5 on 2020-04-28 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('establishment', '0002_auto_20200428_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='establishment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='establishment.Establishment'),
        ),
    ]
