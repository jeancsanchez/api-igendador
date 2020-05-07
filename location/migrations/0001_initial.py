# Generated by Django 3.0.5 on 2020-05-07 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=0, null=True)),
                ('longitude', models.FloatField(default=0, null=True)),
                ('cep', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(default='Brasil', max_length=30, null=True)),
                ('state', models.CharField(default='Ceara', max_length=40, null=True)),
                ('city', models.CharField(default='Fortaleza', max_length=150, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=150, null=True)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='locations', to='establishment.Establishment')),
            ],
            options={
                'db_table': 'tb_location',
            },
        ),
    ]
