# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instanalysis', '0025_auto_20160617_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramlocation',
            name='name',
            field=models.CharField(db_index=True, max_length=300),
        ),
    ]
