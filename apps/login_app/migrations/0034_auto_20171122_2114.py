# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 21:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0033_auto_20171122_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 11, 22, 21, 14, 59, 315728), verbose_name='YYYY-MM-DD'),
        ),
    ]
