# Generated by Django 5.1.6 on 2025-02-20 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnumerationType',
            fields=[
                ('enumTypeId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'EnumerationType',
            },
        ),
        migrations.CreateModel(
            name='Enumeration',
            fields=[
                ('enumId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('parent_enum_id', models.CharField(blank=True, max_length=40, null=True)),
                ('enum_code', models.CharField(blank=True, max_length=255, null=True)),
                ('sequence_num', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('enum_type_id', models.ForeignKey(blank=True, db_column='ENUM_TYPE_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='GeneralModels.enumerationtype')),
            ],
            options={
                'db_table': 'Enumeration',
            },
        ),
    ]
