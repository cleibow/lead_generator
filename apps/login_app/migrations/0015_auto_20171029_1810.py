# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 18:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0014_auto_20171029_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 10, 29, 18, 10, 4, 888123), verbose_name='YYYY-MM-DD'),
        ),
    ]
