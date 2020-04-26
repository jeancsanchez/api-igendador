# Generated by Django 3.0.5 on 2020-04-26 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daybook', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('hour', models.TimeField(auto_now=True)),
                ('day_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='daybook.DayBook')),
                (
                    'user',
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_event',
            },
        ),
    ]
