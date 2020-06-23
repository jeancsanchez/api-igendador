# Generated by Django 2.2.2 on 2020-06-23 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('establishment', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyDiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('month_year', models.IntegerField(
                    choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'),
                             (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'),
                             (12, 'December')], default=1)),
                ('weekday', models.IntegerField(
                    choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'),
                             (6, 'Friday'), (7, 'Saturday')], default=1)),
                ('year', models.IntegerField(default=2020)),
                ('vacancy',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='establishment.Vacancy')),
            ],
            options={
                'db_table': 'tb_monthly_diary',
                'unique_together': {('vacancy', 'weekday', 'month_year', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('name_holiday', models.CharField(max_length=255)),
                ('monthly_diary',
                 models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='monthly_diary.MonthlyDiary')),
            ],
            options={
                'db_table': 'tb_holiday',
            },
        ),
    ]