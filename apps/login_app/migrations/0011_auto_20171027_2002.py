# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0010_auto_20171027_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 10, 27, 20, 2, 40, 801438), verbose_name='YYYY-MM-DD'),
        ),
    ]