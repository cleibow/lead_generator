# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 17:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0012_auto_20171029_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 10, 29, 17, 20, 14, 772962), verbose_name='YYYY-MM-DD'),
        ),
    ]
