# Generated by Django 5.0.1 on 2024-02-20 15:28

import django.contrib.postgres.fields
import django.contrib.postgres.fields.citext
import django.contrib.postgres.fields.hstore
import django.contrib.postgres.fields.ranges
import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PGSProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('platforms', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None), size=None, verbose_name='Используемые платформы')),
            ],
        ),
        migrations.CreateModel(
            name='PGSProject2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('platforms', django.contrib.postgres.fields.hstore.HStoreField(verbose_name='Используемые платформы')),
            ],
        ),
        migrations.CreateModel(
            name='PGSProject3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.citext.CICharField(max_length=40, verbose_name='Название')),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='PGSRoomReserving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Помещение')),
                ('reserving', django.contrib.postgres.fields.ranges.DateTimeRangeField(verbose_name='Время резервирования')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Отменить резервирование')),
            ],
            options={
                'indexes': [django.contrib.postgres.indexes.GistIndex(fields=['reserving'], fillfactor=50, name='i_pgsrr_reserving', opclasses=('range_ops',))],
            },
        ),
        migrations.CreateModel(
            name='PGSRubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None, verbose_name='Теги')),
            ],
            options={
                'indexes': [models.Index(fields=['name', 'description'], name='i_pgsrubric_name_description', opclasses=('varchar_pattern_ops', 'bpchar_pattern_ops'))],
            },
        ),
        migrations.DeleteModel(
            name='PrivateMessage',
        ),
    ]