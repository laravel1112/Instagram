# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instanalysis', '0010_auto_20160517_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagramlocation',
            name='next_url',
        ),
    ]