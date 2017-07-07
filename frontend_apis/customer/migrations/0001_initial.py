# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-07 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_type', models.CharField(blank=True, max_length=50, null=True)),
                ('log_data', models.TextField()),
            ],
            options={
                'db_table': 'data_log',
            },
        ),
    ]
