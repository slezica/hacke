# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161126_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=3000),
        ),
    ]