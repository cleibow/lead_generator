# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_favorites', to='login_app.User'),
        ),
    ]
