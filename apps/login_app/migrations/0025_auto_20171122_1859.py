# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 18:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0024_auto_20171122_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 11, 22, 18, 59, 39, 180363), verbose_name='YYYY-MM-DD'),
        ),
    ]
