# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instanalysis', '0021_auto_20160616_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='is_adhoc',
            field=models.BooleanField(default=False),
        ),
    ]
