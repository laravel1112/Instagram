# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instanalysis', '0022_auto_20160616_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramlocation',
            name='spot',
            field=models.ForeignKey(help_text=b'Spot where this location is associated.', on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='instanalysis.Spot'),
        ),
    ]
