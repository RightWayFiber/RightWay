# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_remove_job_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]