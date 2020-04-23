# Generated by Django 2.2.2 on 2020-04-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('stars', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'tb_establishment',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=300, unique=True)),
                ('establishment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='establishment.Establishment')),
            ],
            options={
                'db_table': 'tb_photo',
            },
        ),
    ]
